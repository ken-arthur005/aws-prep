import type { DomainId } from "./types";

export type RevisionTopic = {
  id: string;
  title: string;
  domain: DomainId;
  guide: string;
  keywords: string[];
  idea: string;
  analogy: string;
  choices: { service: string; when: string; watch: string }[];
  rules: string[];
  scenario: { prompt: string; answer: string; why: string; instead: string };
  reference: string;
};

// Original concise study summaries, informed by the supplied topic guides and AWS references.
// Comparisons and recall cards are derived from these same entries, not separately copied facts.
export const REVISION_REVIEWED = "2026-11-03";
export const REVISION_TOPICS: RevisionTopic[] = [
  {
    id: "iam",
    title: "IAM: who can do what?",
    domain: "secure",
    guide: "01-IAM.md",
    keywords: [
      "iam",
      "sts",
      "assume role",
      "assumerole",
      "instance profile",
      "permission boundary",
      "access keys",
      "identity center",
      "federation",
    ],
    idea: "An identity tells AWS who is asking. Policies determine what that identity may do. Roles provide temporary credentials, so applications do not need long-lived access keys.",
    analogy:
      "A role is a visitor badge: its permissions say which doors open; its trust policy says who may wear it.",
    choices: [
      {
        service: "IAM role + STS",
        when: "Compute, federated users, or another account needs temporary AWS access.",
        watch:
          "The caller must be allowed to assume the role, and the role must trust that caller.",
      },
      {
        service: "Permissions boundary",
        when: "Developers can create identities, but their maximum permissions must be capped.",
        watch: "A boundary limits permissions; it does not grant them.",
      },
      {
        service: "IAM Identity Center",
        when: "Employees need SSO across AWS accounts using a corporate directory.",
        watch:
          "Customer sign-in to your application is usually Cognito territory.",
      },
    ],
    rules: [
      "An applicable explicit deny overrides an allow. An absent allow can also explain AccessDenied.",
      "Give EC2 an instance profile, Lambda an execution role, and ECS application code a task role.",
      "Cross-account access requires the appropriate trust/resource permissions as well as caller permissions. Do not treat all policies as a simple chain of mandatory allows.",
    ],
    scenario: {
      prompt:
        "An EC2 application stores access keys in a configuration file to read S3. Improve security with minimal credential maintenance.",
      answer: "Attach a least-privilege instance role.",
      why: "The SDK obtains automatically rotated temporary credentials from the instance role.",
      instead:
        "Secrets Manager fits a database password that the application must retrieve and rotate; it is not the replacement for an instance role.",
    },
    reference: "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html",
  },
  {
    id: "s3",
    title: "S3: choose storage by access and retrieval",
    domain: "cost",
    guide: "02-S3.md",
    keywords: [
      "s3",
      "glacier",
      "storage class",
      "intelligent-tiering",
      "lifecycle",
      "multipart",
      "object lock",
      "presigned",
    ],
    idea: "S3 stores objects accessed through an API. Choose a class by access frequency, retrieval deadline, resilience needs, and minimum-duration/retrieval charges—not storage price alone.",
    analogy:
      "Standard is a desk drawer; archival classes are an off-site archive. Cheap shelf space is only useful if the archive can return your file in time.",
    choices: [
      {
        service: "Standard / Intelligent-Tiering",
        when: "Hot or short-lived data / unpredictable access patterns respectively.",
        watch:
          "Intelligent-Tiering has monitoring charges for eligible objects; optional archive tiers require restore.",
      },
      {
        service: "Standard-IA / One Zone-IA",
        when: "Infrequent access with milliseconds retrieval; use one zone only when its loss is acceptable.",
        watch:
          "Minimum storage-duration and retrieval charges apply. One Zone-IA does not survive destruction of its AZ.",
      },
      {
        service: "Glacier Instant / Flexible / Deep Archive",
        when: "Archive data: milliseconds / minutes-to-hours / hours retrieval respectively.",
        watch:
          "Flexible expedited retrieval may require provisioned capacity for assured availability. Deep Archive standard retrieval is typically within 12 hours, bulk within 48.",
      },
    ],
    rules: [
      "S3 provides strong read-after-write and list consistency. Older eventual-consistency notes are outdated.",
      "Versioning helps recover overwrites/deletes. Object Lock adds WORM retention and can be enabled on existing versioned buckets; compliance mode prevents deletion of protected versions even by root.",
      "CRR/SRR handle eligible new writes; use Batch Replication for existing objects. Default encryption changes do not rewrite existing objects.",
      "The current multipart quota table lists a maximum object size of 48.8 TiB; multipart upload is required above the single-PUT limit. Check current limits rather than memorising the old 5 TB cap.",
    ],
    scenario: {
      prompt:
        "A seven-year financial archive is rarely read; retrieval within 24 hours is acceptable. Minimise storage cost while retaining multi-AZ resilience.",
      answer: "Consider Glacier Deep Archive with a suitable retrieval option.",
      why: "The relaxed retrieval deadline admits archival storage; One Zone-IA would sacrifice the requested AZ resilience.",
      instead:
        "If records must be immediately accessible, Glacier Instant Retrieval or an online class becomes the candidate. Calculate retrieval and minimum-duration charges too.",
    },
    reference:
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
  },
  {
    id: "ec2",
    title: "EC2: capacity, cost, and placement",
    domain: "cost",
    guide: "03-EC2.md",
    keywords: [
      "ec2",
      "spot",
      "reserved instance",
      "savings plan",
      "dedicated host",
      "placement group",
      "graviton",
      "cpu credit",
      "capacity reservation",
      "instance store",
    ],
    idea: "Separate the machine you need from how you pay for it. A discount is not necessarily a capacity guarantee, and the cheapest interruptible instance cannot satisfy an uninterrupted workload.",
    analogy:
      "On-Demand is a daily rental, a Savings Plan is a spending commitment, and Spot is a cheap standby ticket that can be reclaimed.",
    choices: [
      {
        service: "On-Demand / Capacity Reservation",
        when: "No long commitment / guaranteed capacity in a specified AZ.",
        watch:
          "A capacity reservation and a billing discount solve different problems.",
      },
      {
        service: "Savings Plans / Reserved Instances",
        when: "A predictable baseline justifies a one- or three-year commitment.",
        watch:
          "Compute Savings Plans cover eligible EC2, Fargate, and Lambda usage; they do not reserve capacity.",
      },
      {
        service: "Spot",
        when: "Work can checkpoint, retry, or tolerate interruptions.",
        watch:
          "Use diversified capacity and graceful interruption handling. It is not a fit for an uninterruptible requirement.",
      },
      {
        service: "Dedicated Host",
        when: "Licensing requires physical sockets/cores or host visibility.",
        watch:
          "Dedicated Instances provide isolation without the same host-placement and licensing controls.",
      },
    ],
    rules: [
      "Cluster placement favours closely placed instances in one AZ; spread isolates a small number of critical instances; partition separates groups for distributed systems. A cluster is not a same-rack guarantee.",
      "T-family performance depends on credits and Standard/Unlimited mode. Check sustained load and overage costs.",
      "Instance-store data survives reboot but not stop/termination or host failure. Public IPv4 addresses, including in-use Elastic IPs, are chargeable.",
    ],
    scenario: {
      prompt:
        "A nightly rendering job can checkpoint and restart. Reduce compute cost.",
      answer: "Use a diversified Spot fleet with checkpointing.",
      why: "The explicit interruption tolerance makes spare capacity usable.",
      instead:
        "An uninterruptible short-term workload points toward On-Demand; a sustained baseline can justify a commitment discount.",
    },
    reference:
      "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html",
  },
  {
    id: "block-file",
    title: "EBS, EFS, and instance store",
    domain: "performance",
    guide: "04-EBS-EFS-InstanceStore.md",
    keywords: [
      "ebs",
      "efs",
      "gp3",
      "gp2",
      "io2",
      "io1",
      "st1",
      "sc1",
      "block storage",
      "shared file",
      "instance store",
      "snapshot",
    ],
    idea: "First decide whether you need a block device, a shared filesystem, or disposable local storage. Then match random IOPS, sequential throughput, persistence, and failure scope.",
    analogy:
      "EBS is a detachable disk in one building; EFS is a shared filing cabinet; instance store is scratch paper attached to a desk.",
    choices: [
      {
        service: "EBS gp3 / io2",
        when: "Persistent block storage, boot disks, and databases; io2 targets demanding latency/IOPS/durability requirements.",
        watch:
          "Volumes are AZ-scoped. Current gp3 supports up to 80,000 IOPS on supported configurations, so the old 16,000 dividing line is outdated.",
      },
      {
        service: "EFS",
        when: "Many Linux clients need the same NFS files; Regional EFS supports multi-AZ resilience.",
        watch:
          "One Zone EFS has a different failure scope. Windows SMB requirements call for an appropriate FSx service.",
      },
      {
        service: "Instance store",
        when: "Fast disposable scratch/cache, or data replicated by the application.",
        watch: "Do not rely on it as the only persistent copy.",
      },
      {
        service: "st1 / sc1",
        when: "Large sequential HDD workloads, frequently / infrequently accessed.",
        watch:
          "HDD volumes cannot be boot volumes. Low cost per GB does not imply good random-I/O performance.",
      },
    ],
    rules: [
      "Move an EBS volume across AZs using a snapshot and a new volume. Multi-Attach is restricted to supported io1/io2 configurations in one AZ and requires coordinated software.",
      "To encrypt an unencrypted EBS volume, create a new encrypted volume using a snapshot; an encrypted snapshot copy is one valid route. You cannot encrypt the existing volume in place.",
      "Snapshots are incremental. Fast Snapshot Restore or provisioned initialization avoids the usual first-read initialization penalty, at additional cost.",
    ],
    scenario: {
      prompt:
        "An Auto Scaling fleet of Linux web servers must share uploaded files even as instances are replaced.",
      answer:
        "Use Regional EFS with mount targets and suitable security groups.",
      why: "The application needs a shared NFS filesystem independent of any one instance.",
      instead:
        "EBS fits an AZ-local block device; S3 fits objects if the application can use its object API instead of filesystem semantics.",
    },
    reference:
      "https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html",
  },
  {
    id: "load-balancing",
    title: "Load balancing and Auto Scaling",
    domain: "resilient",
    guide: "05-ELB-AutoScaling.md",
    keywords: [
      "load balancer",
      "alb",
      "nlb",
      "target group",
      "auto scaling",
      "autoscaling",
      "health check",
      "cooldown",
      "deregistration",
      "launch template",
    ],
    idea: "A load balancer directs traffic; an Auto Scaling group maintains and adjusts capacity. Routing away from an unhealthy app and replacing its instance are separate actions.",
    analogy:
      "The host seats customers at healthy tables; the manager adds tables and replaces broken ones.",
    choices: [
      {
        service: "ALB",
        when: "HTTP(S), host/path/header routing, or WAF integration.",
        watch: "It exposes a DNS name, not fixed per-AZ Elastic IPs.",
      },
      {
        service: "NLB",
        when: "TCP/UDP/TLS, static per-AZ addresses, or supported PrivateLink endpoint services.",
        watch: "Layer-4 forwarding does not perform HTTP path-based routing.",
      },
      {
        service: "Gateway Load Balancer",
        when: "Traffic must traverse a fleet of virtual network appliances.",
        watch:
          "GENEVE transports traffic to appliances; this is not an application URL router.",
      },
      {
        service: "Target tracking / scheduled scaling",
        when: "Maintain a metric target / prepare for a known calendar event.",
        watch:
          "Use backlog per worker for queued work; raw CPU may not express outstanding demand.",
      },
    ],
    rules: [
      "Enable ELB health checks on an ASG if app-level failure must trigger instance replacement; EC2 status checks alone can miss a broken application.",
      "Use launch templates. Warm-up, cooldown, and deregistration delay address different phases: new capacity, repeated scaling actions, and draining old targets.",
      "A load-balancer health check needs the correct path, port, expected response, and network access. Opening port 80 alone does not prove the app is healthy.",
    ],
    scenario: {
      prompt:
        "ALB marks a running instance unhealthy, but the ASG leaves it in service indefinitely.",
      answer:
        "Configure the ASG to use ELB health checks, with appropriate grace periods.",
      why: "The ASG must receive the application's health verdict to replace app-broken instances.",
      instead:
        "If the health check itself uses the wrong path or port, repair that check first; replacing healthy instances would hide the real problem.",
    },
    reference:
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html",
  },
  {
    id: "vpc",
    title: "VPC: routes, NAT, and endpoints",
    domain: "secure",
    guide: "06-VPC.md",
    keywords: [
      "vpc",
      "subnet",
      "nat gateway",
      "internet gateway",
      "endpoint",
      "cidr",
      "private ip",
      "ipv6",
    ],
    idea: "A route decides where traffic goes. A firewall decides whether it is allowed. Private connectivity to an AWS service often removes the need to send that traffic through NAT.",
    analogy:
      "Route tables are road signs; endpoints are private hallways; NAT is an outbound receptionist who remembers requested replies.",
    choices: [
      {
        service: "Public NAT gateway",
        when: "Private IPv4 resources must initiate connections to internet services.",
        watch:
          "Place it in a public subnet with an Elastic IP and an IGW route. It does not accept unsolicited inbound internet connections.",
      },
      {
        service: "Gateway endpoint",
        when: "VPC-local S3 or DynamoDB access without gateway-endpoint charges.",
        watch:
          "It is route-table based and cannot be directly used from on-premises or a peered VPC.",
      },
      {
        service: "Interface endpoint",
        when: "A supported service must be reached through private ENIs, including suitable hybrid-access designs.",
        watch:
          "Consider endpoint security groups, DNS, routes, and hourly/data-processing charges.",
      },
      {
        service: "Egress-only IGW",
        when: "IPv6 needs outbound initiation without unsolicited inbound access.",
        watch:
          "Do not assume all IPv6 addresses are public. NAT64 is a separate IPv6-to-IPv4 connectivity pattern.",
      },
    ],
    rules: [
      "A VPC is regional; each subnet is in one AZ. For IPv4 AWS reserves five addresses in each ordinary subnet.",
      "A public subnet has an internet-gateway route; an instance still needs suitable addressing and firewall rules for direct internet access.",
      "For zonal NAT gateways, route each private AZ through its own NAT for AZ resilience and to avoid unnecessary cross-AZ traffic. Account for newer regional NAT designs when explicitly offered.",
    ],
    scenario: {
      prompt:
        "Private EC2 instances upload large files to S3 in the same Region. Reduce NAT processing cost.",
      answer:
        "Use an S3 gateway endpoint and the correct route tables and endpoint/bucket policies.",
      why: "S3 traffic can use the gateway endpoint instead of the paid NAT path.",
      instead:
        "An on-premises client needing private S3 access may require an S3 interface endpoint and hybrid DNS rather than a gateway endpoint.",
    },
    reference:
      "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html",
  },
  {
    id: "dns",
    title: "Route 53: choose the routing rule",
    domain: "performance",
    guide: "07-Route53.md",
    keywords: [
      "route 53",
      "route53",
      "dns",
      "cname",
      "alias",
      "geolocation",
      "geoproximity",
      "hosted zone",
      "resolver",
    ],
    idea: "DNS returns an address; it does not carry the subsequent application traffic. Choose routing based on the business rule, and remember that cached answers affect failover.",
    analogy:
      "A phonebook tells you the number. It cannot redirect a call already being made to an old number.",
    choices: [
      {
        service: "Alias / CNAME",
        when: "Alias for a supported AWS target at the apex; CNAME for another name on a suitable subdomain.",
        watch:
          "CNAME is not allowed at a zone apex. Alias is an A/AAAA-style AWS extension with supported targets.",
      },
      {
        service: "Latency / geolocation / geoproximity",
        when: "Best measured regional latency / location rule / resource distance with optional bias.",
        watch:
          "Closest on a map is not necessarily fastest. Geolocation is not a guarantee of regulatory data residency.",
      },
      {
        service: "Weighted / failover",
        when: "Distribute by assigned weights / primary-secondary health-based routing.",
        watch:
          "DNS caching means weights are not exact per-request percentages and failover is not instantaneous.",
      },
    ],
    rules: [
      "Public health checkers cannot directly probe a private IP; an appropriate CloudWatch-alarm health check can represent private-resource health.",
      "Resolver inbound endpoints let on-premises query AWS private names; outbound endpoints forward suitable AWS queries to on-premises DNS.",
      "Private hosted zones require the appropriate VPC associations and resolver configuration; DNS resolution does not grant network access.",
    ],
    scenario: {
      prompt: "Both example.com and www.example.com must resolve to an ALB.",
      answer:
        "Use an alias at the apex; www may use a suitable alias or CNAME.",
      why: "The apex cannot be a CNAME, and an ALB's changing addresses should not be hardcoded.",
      instead:
        "A CNAME is valid for a suitable subdomain pointing to another hostname.",
    },
    reference:
      "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html",
  },
  {
    id: "edge",
    title: "CloudFront vs Global Accelerator",
    domain: "performance",
    guide: "08-CloudFront-GlobalAccelerator.md",
    keywords: [
      "cloudfront",
      "global accelerator",
      "cdn",
      "edge location",
      "signed cookie",
      "signed url",
      "origin access",
      "transfer acceleration",
    ],
    idea: "CloudFront can cache content near viewers and accelerate HTTP(S). Global Accelerator improves the network path to supported regional TCP/UDP endpoints without caching application data.",
    analogy:
      "CloudFront is a local shop stocking popular books; Global Accelerator is an express road to the original warehouse.",
    choices: [
      {
        service: "CloudFront",
        when: "HTTP(S) delivery, cacheable content, edge logic, or private S3 content.",
        watch:
          "It also supports dynamic content. OAC works with an S3 bucket origin, not an S3 website endpoint.",
      },
      {
        service: "Global Accelerator",
        when: "Supported global TCP/UDP applications need stable anycast addresses and health-based regional routing.",
        watch:
          "No content caching; it does not itself make the application or data multi-region.",
      },
      {
        service: "S3 Transfer Acceleration",
        when: "Distant clients transfer data to/from an S3 bucket through the acceleration endpoint.",
        watch:
          "Benchmark improvement. This is not a general-purpose CDN for your application.",
      },
    ],
    rules: [
      "CloudFront signed URLs grant access using individual URLs; signed cookies are convenient for sets of restricted files. Neither replaces origin access restrictions.",
      "Use OAC and a restrictive bucket policy to prevent direct public S3 access. A CloudFront ACM viewer certificate belongs in us-east-1.",
      "Origin groups provide supported origin failover; cache TTL and versioned filenames govern freshness. Do not equate all caching with immediately fresh content.",
    ],
    scenario: {
      prompt:
        "A global UDP game requires a small stable set of entry IPs and regional failover.",
      answer:
        "Use Global Accelerator with supported regional endpoints and a resilient backend.",
      why: "UDP and stable global entry addresses distinguish it from the usual HTTP CDN design.",
      instead:
        "A global image/video website benefits from CloudFront caching; private S3 delivery adds OAC.",
    },
    reference:
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html",
  },
  {
    id: "rds",
    title: "RDS and Aurora: availability vs reads",
    domain: "resilient",
    guide: "09-RDS-Aurora.md",
    keywords: [
      "rds",
      "aurora",
      "read replica",
      "multi-az",
      "relational",
      "mysql",
      "postgres",
      "database connection",
      "rds proxy",
    ],
    idea: "Availability, read scaling, and connection pooling are different needs. Identify the deployment type before deciding whether an extra database instance is readable or a failover target.",
    analogy:
      "A traditional standby is a spare tyre; read replicas are extra checkout lanes; a connection proxy manages the queue at the checkout.",
    choices: [
      {
        service: "RDS Multi-AZ DB instance",
        when: "A primary needs a synchronous standby and managed AZ failover.",
        watch:
          "The standby does not serve read traffic. This statement is specific to the DB instance deployment.",
      },
      {
        service: "RDS Multi-AZ DB cluster",
        when: "Supported engines need HA plus two readable instances across three AZs.",
        watch:
          "It uses semisynchronous replication and is not an Aurora cluster.",
      },
      {
        service: "Read replica / RDS Proxy",
        when: "Offload supported read workloads / pool and reuse database connections respectively.",
        watch:
          "A traditional RDS read replica is asynchronously replicated; a proxy is not a cache or a read replica.",
      },
      {
        service: "Aurora Global Database",
        when: "A compatible relational application needs low-lag cross-region replication and recovery.",
        watch:
          "Treat recovery objectives as design targets, not unconditional guarantees. Plan promotion, endpoints, and application recovery.",
      },
    ],
    rules: [
      "Aurora separates compute from multi-AZ storage. Writer and reader endpoints serve different connection roles.",
      "Encrypt an unencrypted RDS database through a snapshot, encrypted snapshot copy, and restore; update clients to the new database.",
      "Automated backup retention supports PITR up to 35 days; retained automated backups and AWS Backup can change deletion/retention behaviour. Manual snapshots are another long-term backup option.",
    ],
    scenario: {
      prompt:
        "Reports overload the primary RDS database. The team proposes querying its traditional Multi-AZ standby.",
      answer: "Route suitable reporting reads to a read replica instead.",
      why: "That standby is a failover component, not a readable endpoint.",
      instead:
        "An explicitly stated Multi-AZ DB cluster has readable instances. Repeated identical queries may favour caching; connection exhaustion favours RDS Proxy.",
    },
    reference:
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html",
  },
  {
    id: "dynamodb",
    title: "DynamoDB: keys, capacity, and changes",
    domain: "performance",
    guide: "10-DynamoDB.md",
    keywords: [
      "dynamodb",
      "dynamo db",
      "dax",
      "partition key",
      "global table",
      "secondary index",
      "rcu",
      "wcu",
    ],
    idea: "DynamoDB is a managed key-value/document database. Design keys around access patterns and distribute traffic; serverless does not remove hot-key or quota constraints.",
    analogy:
      "A good partition key is a numbered coat-check ticket: it takes you directly to the right hook instead of searching every coat.",
    choices: [
      {
        service: "On-demand / provisioned",
        when: "Variable request-based demand / planned capacity with optional auto scaling.",
        watch:
          "Neither removes hot-partition limits. Choose with workload evidence and current pricing.",
      },
      {
        service: "GSI / LSI",
        when: "A new partition/sort-key access pattern / alternate sort key with the same partition key.",
        watch:
          "LSIs must be created with the table; GSIs may be added later. GSI reads are eventually consistent.",
      },
      {
        service: "Streams / Global Tables",
        when: "React to item changes / support multi-region reads and writes.",
        watch:
          "Streams retain records for 24 hours. Current Global Tables offer eventual and supported strong-consistency modes with different constraints.",
      },
      {
        service: "DAX",
        when: "Supported DynamoDB read patterns need an in-memory cache.",
        watch:
          "Use a DAX client/configuration; it is not literally zero integration work. Strong reads do not gain the normal cache benefit.",
      },
    ],
    rules: [
      "The item limit is 400 KB. Store larger binary payloads in S3 and retain a reference in the table.",
      "TTL deletion is asynchronous, not a precise timer or access-control expiry. Applications must reject logically expired data when timing matters.",
      "One RCU buys one strong or two eventual reads/second up to 4 KB; one WCU buys one write/second up to 1 KB. Transactions consume additional capacity.",
    ],
    scenario: {
      prompt:
        "An existing table keyed by user ID must also support lookup by email.",
      answer: "Add an appropriate global secondary index.",
      why: "It creates the required access path after table creation without scanning every item.",
      instead:
        "An LSI suits an alternate sort key with the same partition key, but it must be defined when creating the table.",
    },
    reference:
      "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html",
  },
  {
    id: "cache",
    title: "Caching: hot reads and shared sessions",
    domain: "performance",
    guide: "11-ElastiCache.md",
    keywords: [
      "elasticache",
      "redis",
      "valkey",
      "memcached",
      "cache",
      "caching",
      "session state",
      "leaderboard",
      "sorted set",
    ],
    idea: "A cache reuses a result instead of recomputing or rereading it. A shared session store also lets an application server disappear without taking the user's session with it.",
    analogy:
      "A librarian puts a frequently requested answer on a sticky note. The hard part is keeping the note valid when the original answer changes.",
    choices: [
      {
        service: "ElastiCache for Valkey / Redis OSS",
        when: "Rich data structures, sorted sets, shared sessions, and supported replication/failover designs.",
        watch:
          "Asynchronous replication and failover are not a promise of zero data loss.",
      },
      {
        service: "Memcached",
        when: "A simple distributed object cache is sufficient.",
        watch:
          "Node-based and serverless offerings differ; do not apply all old node-based limitations universally.",
      },
      {
        service: "Read replica",
        when: "Suitable read queries should run on a separate database copy.",
        watch:
          "A replica still executes queries; a cache reuses results. Both require a freshness strategy.",
      },
    ],
    rules: [
      "Cache-aside fills on a miss; write-through updates on the write path. Neither alone is an absolute freshness guarantee under failures or out-of-band writes.",
      "TTL limits cache lifetime but does not prove a cached price is current. Design invalidation for strict freshness requirements.",
      "Externalise session state to make web instances replaceable; sticky sessions alone do not survive losing the server holding the session.",
    ],
    scenario: {
      prompt: "Users lose their sessions whenever the ASG scales in.",
      answer:
        "Move session state to a suitable shared store such as ElastiCache or DynamoDB.",
      why: "Any surviving server can retrieve the session independently of the terminated instance.",
      instead:
        "ALB stickiness can keep requests on one instance but cannot preserve that instance's in-memory session after termination.",
    },
    reference:
      "https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html",
  },
  {
    id: "analytics",
    title: "Analytics and specialised databases",
    domain: "performance",
    guide: "12-Other-Databases.md",
    keywords: [
      "athena",
      "redshift",
      "spectrum",
      "neptune",
      "documentdb",
      "keyspaces",
      "opensearch",
      "parquet",
      "data warehouse",
      "olap",
      "timestream",
      "qldb",
    ],
    idea: "Start with the data shape and the operation: SQL on files, warehouse analytics, graph traversal, document compatibility, and text search are different jobs.",
    analogy:
      "A warehouse, a relationship map, and a search index organise the same information for different questions.",
    choices: [
      {
        service: "Athena / Redshift",
        when: "SQL over supported data sources including S3 / a managed analytics warehouse.",
        watch:
          "Athena is not limited to one file; Redshift Spectrum can query external S3 data without loading it into local tables.",
      },
      {
        service: "Neptune / OpenSearch",
        when: "Graph relationships / full-text search and search analytics.",
        watch:
          "A graph relationship problem is not simply a string-search problem.",
      },
      {
        service: "DocumentDB / Keyspaces",
        when: "A supported MongoDB-compatible / Cassandra-compatible workload.",
        watch:
          "Compatibility needs assessment; do not assume every source-engine feature or workload migrates unchanged.",
      },
    ],
    rules: [
      "For Athena, partition pruning, suitable columnar formats such as Parquet/ORC, compression, and appropriate file sizes reduce unnecessary scanning.",
      "Keep heavy analytical scans from overwhelming an OLTP system; choose read replicas, export pipelines, or a warehouse according to the query and freshness requirements.",
      "QLDB reached end of support in July 2025. Older ledger keyword questions need historical context rather than a current QLDB recommendation.",
    ],
    scenario: {
      prompt:
        "Occasional SQL analysis of large JSON logs in S3 is slow and expensive.",
      answer:
        "Consider Athena with partitioned, suitably sized columnar files and appropriate compression.",
      why: "Reading only the necessary partitions and columns reduces scanned data.",
      instead:
        "An established warehouse serving repeated BI workloads may favour Redshift; fuzzy product search calls for a search index.",
    },
    reference:
      "https://docs.aws.amazon.com/athena/latest/ug/performance-tuning.html",
  },
  {
    id: "lambda",
    title: "Lambda: events and concurrency",
    domain: "performance",
    guide: "13-Lambda.md",
    keywords: [
      "lambda",
      "concurrency",
      "cold start",
      "serverless function",
      "lambda@edge",
      "cloudfront function",
    ],
    idea: "Lambda runs event-triggered code without managing servers. Distinguish execution limits, invocation/retry models, permissions, and controls on parallel execution.",
    analogy:
      "A contractor arrives for each job. Reserved concurrency allocates and caps contractors; provisioned concurrency keeps an allocated team ready to start quickly.",
    choices: [
      {
        service: "Reserved concurrency",
        when: "Reserve execution capacity and bound a function's concurrent invocations.",
        watch:
          "It does not pre-warm execution environments or pool database connections.",
      },
      {
        service: "Provisioned concurrency",
        when: "Predictable startup latency justifies paying for ready environments.",
        watch:
          "Costs apply while provisioned; traffic above provisioned capacity can still experience cold starts.",
      },
      {
        service: "Batch / ECS tasks",
        when: "One indivisible job exceeds Lambda's 15-minute invocation limit.",
        watch:
          "Step Functions can orchestrate work but does not extend the runtime limit of an individual Lambda invocation.",
      },
    ],
    rules: [
      "Increasing memory also allocates more CPU. Benchmark total duration and cost rather than assuming the smallest memory is cheapest.",
      "SQS/Kinesis/DynamoDB event source mappings poll records; retries and failure handling differ from asynchronous push invocation. Design idempotent handlers.",
      "VPC access requires suitable subnet/security-group configuration. A public subnet does not give a Lambda ENI a public IP; use the right NAT or endpoint path.",
    ],
    scenario: {
      prompt:
        "An event-driven function overwhelms a database with thousands of new connections.",
      answer:
        "Use suitable concurrency limits and consider RDS Proxy for supported databases.",
      why: "Bounded parallelism protects the downstream system; a proxy reuses connections.",
      instead:
        "Provisioned concurrency addresses startup latency, not a database's connection budget.",
    },
    reference:
      "https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html",
  },
  {
    id: "containers",
    title: "ECS, EKS, and Fargate",
    domain: "performance",
    guide: "14-ECS-EKS-Fargate.md",
    keywords: [
      "ecs",
      "eks",
      "fargate",
      "kubernetes",
      "container",
      "ecr",
      "task role",
      "execution role",
    ],
    idea: "ECS and EKS orchestrate containers; Fargate supplies managed compute for supported tasks/pods. ECR stores images. These are different layers, not interchangeable competitors.",
    analogy:
      "ECR is the recipe warehouse, ECS/EKS the kitchen manager, and Fargate a rented kitchen where the equipment is maintained for you.",
    choices: [
      {
        service: "ECS + Fargate",
        when: "AWS-native containers should run without managing an EC2 fleet.",
        watch:
          "Task scaling and application design still need configuration; serverless does not mean every scaling policy is automatic.",
      },
      {
        service: "EKS",
        when: "Existing Kubernetes manifests, tooling, or portability are explicit requirements.",
        watch:
          "Choose an appropriate supported compute option; managed control plane does not eliminate every operational responsibility.",
      },
      {
        service: "EC2-backed containers",
        when: "Work needs supported GPUs, host controls, or instance-specific capabilities.",
        watch:
          "You retain instance capacity, patching, and fleet-management responsibilities.",
      },
    ],
    rules: [
      "The ECS task execution role supports launch plumbing such as ECR pulls and logging. The task role authorises application calls to AWS.",
      "Fargate uses awsvpc networking, giving tasks ENIs and security-group controls. Ensure image pull, secrets, logs, and application dependencies have network paths.",
      "A service maintains task count; task definitions describe containers. Use suitable service auto scaling and load-balancer health checks.",
    ],
    scenario: {
      prompt:
        "A team has containerised microservices and wants independent scaling without managing servers. Kubernetes is not a requirement.",
      answer: "Use ECS services on Fargate with suitable scaling policies.",
      why: "It meets the container and operational-overhead requirements without introducing a self-managed instance fleet.",
      instead:
        "Existing Kubernetes tooling or an explicit portability requirement makes EKS a stronger candidate.",
    },
    reference:
      "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html",
  },
  {
    id: "beanstalk",
    title: "Elastic Beanstalk: managed application environments",
    domain: "resilient",
    guide: "15-Elastic-Beanstalk.md",
    keywords: [
      "beanstalk",
      ".ebextensions",
      "immutable deployment",
      "rolling deployment",
      "blue/green",
      "cname swap",
    ],
    idea: "Beanstalk assembles and manages a conventional application environment while keeping its underlying resources visible and configurable.",
    analogy:
      "A furnished apartment saves setup effort, but you still control the furniture and pay for the rooms.",
    choices: [
      {
        service: "All at once / rolling",
        when: "Downtime is acceptable / deploy in batches on existing capacity.",
        watch:
          "Rolling reduces available capacity; a healthy app and suitable batch settings are still needed to avoid impact.",
      },
      {
        service: "Rolling with additional batch / immutable",
        when: "Maintain capacity with an extra batch / test a new fleet before replacing the old.",
        watch:
          "Extra resources cost money; deployment failure and rollback behaviour differ.",
      },
      {
        service: "Blue/green",
        when: "Test a separate environment before switching its CNAME.",
        watch:
          "DNS caching, database migrations, and shared state make cutover more than an instantaneous universal switch.",
      },
    ],
    rules: [
      "Keep production database lifecycle independent of disposable application environments; inspect retention/deletion settings.",
      "A worker environment consumes SQS work. A web environment serves requests.",
      "Use CloudFormation/CDK for general-purpose infrastructure definition; Beanstalk is application-shaped deployment automation.",
    ],
    scenario: {
      prompt:
        "A new application version must be tested in an isolated environment before routing users to it.",
      answer: "Use blue/green environments and a planned CNAME cutover.",
      why: "The new environment can be validated independently while the old one is still available.",
      instead:
        "Rolling deployment updates batches inside an existing environment rather than providing a separate test environment.",
    },
    reference:
      "https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rolling-version-deploy.html",
  },
  {
    id: "api",
    title: "API Gateway: front door and transformations",
    domain: "performance",
    guide: "16-API-Gateway.md",
    keywords: [
      "api gateway",
      "mapping template",
      "rest api",
      "http api",
      "websocket",
      "cors",
      "usage plan",
      "authorizer",
    ],
    idea: "API Gateway handles API-facing concerns such as routing, authorisation, throttling, and supported transformations. The API type determines available features.",
    analogy:
      "A front desk can check badges and translate forms before handing work to the back office.",
    choices: [
      {
        service: "REST / HTTP / WebSocket API",
        when: "REST-specific features / a lighter HTTP API / persistent bidirectional messaging.",
        watch:
          "Do not assume feature parity: usage plans, mapping templates, caching, and authorisers differ.",
      },
      {
        service: "Mapping templates",
        when: "A supported non-proxy REST integration must transform request/response payloads.",
        watch:
          "Models describe or validate data; they do not by themselves transform a response body.",
      },
      {
        service: "Asynchronous job API",
        when: "Long work should be accepted now and completed later with polling or notification.",
        watch:
          "Return a job ID/accepted status and make submission/retry behaviour explicit.",
      },
    ],
    rules: [
      "The old blanket 29-second maximum is outdated: supported Regional/private REST APIs can request higher integration timeouts, potentially with quota tradeoffs. API type and quotas matter.",
      "API keys and usage plans manage consumption, not strong authentication. Use IAM, Cognito/JWT, or an appropriate Lambda authoriser.",
      "A browser CORS error, an authorisation denial, a throttling 429, and a backend integration timeout require different fixes.",
    ],
    scenario: {
      prompt:
        "Legacy API clients need the old response format after a backend upgrade, without changing that backend.",
      answer:
        "Use suitable API Gateway REST integration response mapping templates.",
      why: "Transformation changes the payload presented to the clients.",
      instead:
        "Caching reuses responses but does not translate their shape; method response models are not a transformation engine.",
    },
    reference:
      "https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html",
  },
  {
    id: "messaging",
    title: "SQS, SNS, Kinesis, and Firehose",
    domain: "resilient",
    guide: "17-SQS-SNS-Kinesis.md",
    keywords: [
      "sqs",
      "sns",
      "kinesis",
      "firehose",
      "queue",
      "fan-out",
      "fanout",
      "visibility timeout",
      "dead-letter",
      "long polling",
      "decoupl",
    ],
    idea: "Queues distribute work, topics notify subscribers, streams retain ordered records for independent readers, and delivery services move streaming data to destinations.",
    analogy:
      "SQS is a work inbox, SNS a distribution list, Kinesis a replayable journal, and Firehose a managed delivery truck.",
    choices: [
      {
        service: "SQS",
        when: "Buffer work and let workers consume independently of producers.",
        watch:
          "Standard delivery can repeat. Visibility hides a message; successful processing must delete it. Consumers should be idempotent.",
      },
      {
        service: "SNS → separate SQS queues",
        when: "Each downstream system needs its own durable backlog of the same notifications.",
        watch:
          "SNS has retries, DLQs, and supported FIFO archive/replay; the old claim that SNS never persists/retries anything is misleading.",
      },
      {
        service: "Kinesis Data Streams",
        when: "Independent consumers need a retained stream with replay and ordering within its partitioning model.",
        watch:
          "Configure retention/capacity and partition keys; not every record has global ordering.",
      },
      {
        service: "Amazon Data Firehose",
        when: "Deliver streaming data to supported destinations with managed buffering/transformation.",
        watch:
          "Buffering and latency depend on configuration and destination; it is not always a fixed 60-second delay.",
      },
    ],
    rules: [
      "SQS supports messages up to 1 MiB; larger payloads can use an S3 reference pattern. Default retention is four days, maximum 14 days.",
      "FIFO ordering is per message group. Deduplication does not make arbitrary downstream side effects magically exactly-once; design idempotency.",
      "For duplicate concurrent processing, check visibility timeout versus processing duration. For empty polling cost, consider long polling (up to 20 seconds). High-throughput FIFO exceeds old 300/3,000 figures under supported settings.",
    ],
    scenario: {
      prompt:
        "Billing, shipping, and fraud processing must each receive every order and tolerate an hour-long consumer outage.",
      answer: "Fan an SNS topic out to a separate SQS queue for each consumer.",
      why: "Each system keeps its own backlog rather than competing for messages in a single queue.",
      instead:
        "A single SQS queue with competing workers distributes work; Kinesis fits independent retained-stream readers and replay requirements.",
    },
    reference:
      "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html",
  },
  {
    id: "events",
    title: "EventBridge and Step Functions",
    domain: "resilient",
    guide: "18-EventBridge-StepFunctions.md",
    keywords: [
      "eventbridge",
      "step functions",
      "state machine",
      "workflow",
      "orchestrat",
      "scheduled rule",
      "human approval",
    ],
    idea: "EventBridge routes events to interested targets. Step Functions coordinates a planned sequence of work, including branching, waiting, retries, and failures.",
    analogy:
      "EventBridge is a switchboard; Step Functions is a checklist manager who follows one job through to completion.",
    choices: [
      {
        service: "EventBridge bus / Scheduler",
        when: "Route supported AWS/SaaS/custom events / invoke a target on a schedule.",
        watch:
          "A schedule and an event-pattern rule are different triggers. Configure retry policies and DLQs.",
      },
      {
        service: "Step Functions Standard",
        when: "A long-running, auditable workflow needs branching or callback/human steps.",
        watch:
          "Maximum execution duration is one year; service task limits still apply.",
      },
      {
        service: "Step Functions Express",
        when: "Short, high-volume workflows fit its execution and integration semantics.",
        watch:
          "Maximum duration is five minutes; check synchronous/asynchronous guarantees and logging.",
      },
    ],
    rules: [
      "Orchestrating multiple Lambda functions does not extend any single function's 15-minute limit. Long indivisible work can run in an ECS/Batch task.",
      "Choice branches, Map iterates, Parallel runs branches, and Retry/Catch define failure handling.",
      "EventBridge archive/replay is a retained-event routing capability, not a substitute for every streaming workload.",
    ],
    scenario: {
      prompt:
        "A payment workflow must retry failed steps, wait two days for approval, and retain execution history.",
      answer:
        "Use Step Functions Standard with suitable callback/wait and retry handling.",
      why: "The workflow is coordinated, long-lived, and auditable.",
      instead:
        "EventBridge routes events to start work but does not by itself define the full stateful approval sequence.",
    },
    reference:
      "https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html",
  },
  {
    id: "observability",
    title: "CloudWatch vs CloudTrail vs Config",
    domain: "secure",
    guide: "19-CloudWatch-CloudTrail-Config.md",
    keywords: [
      "cloudwatch",
      "cloudtrail",
      "aws config",
      "configuration",
      "audit",
      "logging",
      "metric",
      "x-ray",
      "tracing",
      "compliance rule",
    ],
    idea: "Ask whether you need performance evidence, activity evidence, or resource-configuration evidence. These are three different monitoring questions.",
    analogy:
      "CloudWatch is a bedside monitor; CloudTrail is a visitor log; Config is the history of the patient's recorded state and rule checks.",
    choices: [
      {
        service: "CloudWatch",
        when: "Metrics, logs, alarms, and operational investigation.",
        watch:
          "EC2 guest memory/disk-space metrics normally require an agent or another custom collection mechanism.",
      },
      {
        service: "CloudTrail",
        when: "Determine which identity made supported API/activity requests.",
        watch:
          "Free event history covers 90 days of management events. Object data events require the appropriate configuration and incur charges.",
      },
      {
        service: "AWS Config",
        when: "Track supported resource configuration history and evaluate compliance rules.",
        watch:
          "Detection/remediation after a change is not the same as preventing the API action.",
      },
      {
        service: "Distributed tracing",
        when: "Follow a request across service hops to locate latency/errors.",
        watch:
          "Use supported X-Ray/OpenTelemetry integrations; a single CPU alarm does not describe the whole request journey.",
      },
    ],
    rules: [
      "Log integrity validation detects tampering; immutability/retention requires separate controls such as S3 Object Lock.",
      "Config remediation can invoke SSM Automation. SCP/IAM restrictions address prevention.",
      "CloudTrail Lake closed to new customers in May 2026; do not assume a new account can adopt it. Trails/S3 and appropriate query tools are a separate design.",
    ],
    scenario: {
      prompt:
        "Track S3 bucket configuration changes and automatically identify buckets that violate public-access rules.",
      answer: "Use AWS Config recording and appropriate compliance rules.",
      why: "The requirement concerns configuration state and rule evaluation.",
      instead:
        "If the question asks who changed a bucket policy, inspect CloudTrail; if it asks to alarm on CPU, use CloudWatch.",
    },
    reference:
      "https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html",
  },
  {
    id: "keys",
    title: "KMS and CloudHSM: control the keys",
    domain: "secure",
    guide: "20-KMS-CloudHSM.md",
    keywords: [
      "kms",
      "cloudhsm",
      "encryption",
      "encrypt",
      "data key",
      "key policy",
      "fips",
      "bucket key",
      "certificate",
    ],
    idea: "Separate encrypting the data from managing the keys. KMS integrates key control and auditing with AWS; CloudHSM provides dedicated HSMs with customer-managed cryptographic administration.",
    analogy:
      "Envelope encryption uses a small vault key to protect a working key, then the working key encrypts the large file.",
    choices: [
      {
        service: "KMS customer-managed key",
        when: "Control policy, supported rotation, disable/deletion, and audit use through integrated services.",
        watch:
          "Key policies matter. Same-account direct grants and IAM delegation differ; cross-account use typically needs permissions on both sides.",
      },
      {
        service: "Envelope encryption",
        when: "Encrypt a large payload using a data key protected by KMS.",
        watch:
          "KMS Encrypt's symmetric plaintext limit is 4 KB; KMS need not receive the large file.",
      },
      {
        service: "CloudHSM",
        when: "Dedicated HSM hardware and supported cryptographic interfaces/customer administration are explicit needs.",
        watch:
          "Do not choose by an outdated 'KMS is only FIPS Level 2' rule. Current KMS HSMs have FIPS 140-3 Level 3 validation.",
      },
    ],
    rules: [
      "Disabling a key is reversible and stops supported use quickly; scheduling deletion has a 7–30 day waiting period and eventual irreversible consequences.",
      "Customer-managed symmetric key rotation supports configurable periods within supported ranges, not only a yearly switch.",
      "SSE encrypts at rest; TLS protects transit. S3 Bucket Keys reduce KMS request volume and change the granularity of KMS-use events, not S3 data-event audit capabilities.",
    ],
    scenario: {
      prompt: "A 100 MB file must be encrypted with a KMS-controlled key.",
      answer:
        "Use envelope encryption with a generated data key and store its encrypted copy with the ciphertext.",
      why: "The large file is encrypted locally or by the integrated service; KMS protects the much smaller data key.",
      instead:
        "Direct KMS Encrypt is suitable only for supported small plaintext payloads.",
    },
    reference:
      "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html",
  },
  {
    id: "secrets",
    title: "Secrets Manager vs Parameter Store",
    domain: "secure",
    guide: "21-SecretsManager-ParameterStore.md",
    keywords: [
      "secrets manager",
      "parameter store",
      "securestring",
      "password",
      "secret rotation",
      "rotate credentials",
    ],
    idea: "Both store values behind permissions. Choose based on secret lifecycle, rotation, configuration organisation, sharing needs, and cost.",
    analogy:
      "Parameter Store is a labelled configuration cupboard; Secrets Manager adds a managed process for replacing and distributing keys.",
    choices: [
      {
        service: "Secrets Manager",
        when: "Managed secret rotation and supported secret lifecycle/sharing features are required.",
        watch:
          "Rotation support varies by secret type and integration. Applications must refresh values; environment injection does not automatically update a running process.",
      },
      {
        service: "SSM Parameter Store",
        when: "Hierarchical configuration and supported SecureString storage fit the requirement.",
        watch:
          "Standard and advanced tiers have different limits/charges. Advanced parameters can be shared through supported RAM workflows.",
      },
    ],
    rules: [
      "Use an application IAM role to retrieve the value. Storing an access key in a vault does not replace an IAM role for an AWS-hosted workload.",
      "Parameter Store does not offer the same native password-rotation lifecycle as Secrets Manager; notifications/expiration policies are not rotation.",
      "Include KMS permissions and resource policies where applicable; storage access and decrypt access are separate checks.",
    ],
    scenario: {
      prompt:
        "An application must use an RDS password that changes automatically on a schedule.",
      answer:
        "Use a supported Secrets Manager rotation integration and make the application refresh credentials correctly.",
      why: "The requirement is the password lifecycle, not merely encrypted storage.",
      instead:
        "A non-secret configuration value organised by environment may fit Parameter Store at lower cost.",
    },
    reference:
      "https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html",
  },
  {
    id: "security",
    title: "WAF, Shield, and the security services",
    domain: "secure",
    guide: "22-WAF-Shield-SecurityServices.md",
    keywords: [
      "waf",
      "shield",
      "guardduty",
      "macie",
      "inspector",
      "security hub",
      "detective",
      "firewall",
      "ddos",
      "security group",
      "network acl",
      "nacl",
    ],
    idea: "Choose the control by layer and purpose: network permissions, HTTP filtering, DDoS protection, threat detection, vulnerability scanning, or sensitive-data discovery.",
    analogy:
      "A door guard, crowd-control team, detective, and building inspector all provide security but solve different problems.",
    choices: [
      {
        service: "Security group / NACL",
        when: "Stateful allow-only ENI controls / stateless subnet allow-and-deny rules.",
        watch:
          "NACL rule order and return-path ephemeral ports matter. Diagnose inbound versus outbound direction rather than memorising one missing port rule.",
      },
      {
        service: "WAF / Shield",
        when: "Supported HTTP request filtering / DDoS mitigation.",
        watch:
          "WAF attaches to supported resources, not directly to an EC2 instance or NLB. Advanced DDoS features have eligibility and cost-protection conditions.",
      },
      {
        service: "GuardDuty / Inspector / Macie",
        when: "Threat activity / vulnerabilities / sensitive data in S3.",
        watch:
          "Finding a software CVE is not the same as detecting malicious activity or classifying bucket contents.",
      },
      {
        service: "Firewall Manager / Security Hub",
        when: "Central policy rollout / aggregation and supported security-posture workflows.",
        watch:
          "A findings dashboard is not itself the same as enforcing every firewall rule.",
      },
    ],
    rules: [
      "A security group cannot add an explicit deny. A subnet NACL can, but the best IP-blocking control still depends on the resource and protocol in the question.",
      "Flow Logs show traffic metadata, not packet payloads. Traffic Mirroring is a packet-copy capability for supported interfaces.",
      "Separate prevention, detection, investigation, and remediation. Choose the service that performs the requested action.",
    ],
    scenario: {
      prompt:
        "Identify S3 objects containing credit-card details across many buckets.",
      answer: "Use Amazon Macie with appropriate discovery jobs/configuration.",
      why: "The task is sensitive-data discovery in S3.",
      instead:
        "Inspector finds supported software vulnerabilities; GuardDuty detects suspicious activity rather than classifying every object's contents.",
    },
    reference:
      "https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html",
  },
  {
    id: "cognito",
    title: "Cognito: logins vs AWS credentials",
    domain: "secure",
    guide: "23-Cognito.md",
    keywords: [
      "cognito",
      "user pool",
      "identity pool",
      "social login",
      "jwt",
      "customer authentication",
    ],
    idea: "A user pool authenticates application users and issues tokens. An identity pool exchanges supported identities for temporary AWS credentials governed by IAM.",
    analogy:
      "The login desk issues a visitor badge; the credential exchange turns an accepted badge into a key for specific AWS doors.",
    choices: [
      {
        service: "User pool",
        when: "Customer sign-up/sign-in, federation, MFA, and token-based application access.",
        watch: "A JWT is not itself an S3 API credential.",
      },
      {
        service: "Identity pool",
        when: "Supported app identities or guests need scoped temporary AWS credentials.",
        watch:
          "Configure roles and least-privilege resource access; authentication does not imply unrestricted S3 access.",
      },
      {
        service: "IAM Identity Center",
        when: "The workforce needs access to AWS accounts/business applications.",
        watch:
          "Identify the audience and actual access path rather than treating every human login alike.",
      },
    ],
    rules: [
      "API Gateway and ALB have supported Cognito authentication integrations with distinct configuration requirements.",
      "Direct S3 uploads may also use backend-issued presigned URLs; an identity pool is not the only possible design.",
      "Per-user prefix permissions can use appropriate identity context and policy variables.",
    ],
    scenario: {
      prompt:
        "Mobile customers sign in and need direct, limited AWS API access to their own uploaded objects.",
      answer:
        "Use a supported identity-provider flow with Cognito identity pools and narrowly scoped IAM roles.",
      why: "AWS API calls require AWS credentials and appropriate resource permissions.",
      instead:
        "User pools alone provide login tokens; presigned upload URLs are another candidate if a backend can issue scoped URLs.",
    },
    reference:
      "https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html",
  },
  {
    id: "directory",
    title: "Directory services and hybrid identities",
    domain: "secure",
    guide: "24-Directory-Services.md",
    keywords: [
      "active directory",
      "managed microsoft ad",
      "ad connector",
      "simple ad",
      "ldap",
      "directory service",
      "domain join",
    ],
    idea: "An actual directory in AWS, a proxy to an existing directory, and a standalone compatible directory have different capabilities and dependencies.",
    analogy:
      "Managed AD is a branch office; AD Connector is a telephone line back to headquarters; Simple AD is a smaller independent office.",
    choices: [
      {
        service: "AWS Managed Microsoft AD",
        when: "Real Microsoft AD capabilities or supported trust/integration in AWS are needed.",
        watch:
          "Network/DNS/trust requirements still apply; check each consuming service's integration support.",
      },
      {
        service: "AD Connector",
        when: "Supported AWS applications should proxy authentication to an existing self-managed directory.",
        watch:
          "It is not a standalone directory and is not universally supported by every AD-consuming AWS service.",
      },
      {
        service: "Simple AD",
        when: "A small supported standalone AD-compatible directory is sufficient.",
        watch:
          "It does not support the same trust or feature set as Managed Microsoft AD.",
      },
    ],
    rules: [
      "Do not assume AD Connector can be substituted into FSx/RDS designs that require a supported real AD integration.",
      "Hybrid authentication depends on the required network connectivity and DNS resolution.",
      "Workforce SSO to AWS accounts and Windows domain membership are different requirements.",
    ],
    scenario: {
      prompt:
        "Windows applications in AWS need an actual Microsoft directory with a supported trust to on-premises AD.",
      answer:
        "Consider AWS Managed Microsoft AD with the required trust, networking, and DNS.",
      why: "The requirement is a real cloud-resident directory and trust capabilities.",
      instead:
        "AD Connector fits supported proxy-authentication scenarios that keep the existing directory authoritative.",
    },
    reference:
      "https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html",
  },
  {
    id: "hybrid-storage",
    title: "Storage Gateway vs DataSync vs Transfer Family",
    domain: "performance",
    guide: "25-StorageGateway-DataSync-TransferFamily.md",
    keywords: [
      "storage gateway",
      "file gateway",
      "volume gateway",
      "tape gateway",
      "datasync",
      "transfer family",
      "sftp",
      "iscsi",
      "cached volume",
      "stored volume",
    ],
    idea: "An ongoing hybrid access bridge, a managed copy engine, and a managed partner-transfer endpoint are different needs even when all eventually store data in AWS.",
    analogy:
      "Storage Gateway is a cloud-backed cabinet, DataSync the moving company, and Transfer Family the receiving dock.",
    choices: [
      {
        service: "S3 File / Volume / Tape Gateway",
        when: "Ongoing supported file access / iSCSI volumes / a virtual tape library.",
        watch:
          "Cached volumes keep primary data in AWS; stored volumes keep the primary dataset locally and back it up.",
      },
      {
        service: "DataSync",
        when: "Move or periodically synchronise supported file/object storage with managed checking and scheduling.",
        watch:
          "Metadata and permissions preservation depend on source/destination type; an S3 object is not a native NTFS file.",
      },
      {
        service: "Transfer Family",
        when: "Partners use supported transfer protocols while data lands in S3/EFS.",
        watch:
          "Protocol, endpoint, identity-provider, and storage combinations differ. Do not build an EC2 transfer server unless its control is actually needed.",
      },
    ],
    rules: [
      "A migration copies data; a gateway lets an application continue to access cloud-backed storage through a familiar interface.",
      "FSx File Gateway is not available to new customers; do not recommend it unconditionally from old notes.",
      "Assess bandwidth, transfer window, data format, consistency needs, and security before choosing the transport.",
    ],
    scenario: {
      prompt:
        "Partners must keep SFTP scripts, but the company wants no server fleet to manage and files should land in S3.",
      answer:
        "Use an AWS Transfer Family SFTP endpoint with suitable identities and S3 permissions.",
      why: "It preserves the client protocol and manages the server endpoint.",
      instead:
        "DataSync fits scheduled bulk copies between supported storage locations; a File Gateway fits ongoing on-premises file access.",
    },
    reference:
      "https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html",
  },
  {
    id: "fsx",
    title: "FSx: match the filesystem",
    domain: "performance",
    guide: "26-FSx.md",
    keywords: [
      "fsx",
      "lustre",
      "ontap",
      "openzfs",
      "smb",
      "ntfs",
      "snapmirror",
      "hpc",
      "parallel file",
    ],
    idea: "Choose a filesystem by protocol, application compatibility, throughput, latency, and failure requirements—not just the word 'shared'.",
    analogy:
      "FSx offers specialist workshops: each has the tools expected by a particular workload.",
    choices: [
      {
        service: "FSx for Windows File Server",
        when: "Windows SMB/NTFS semantics and supported AD integration.",
        watch:
          "Select Multi-AZ when AZ resilience is required; a Windows client is not automatically an EFS client.",
      },
      {
        service: "FSx for Lustre",
        when: "Parallel HPC/ML processing needs a high-performance filesystem, with supported S3 integration.",
        watch:
          "Scratch and persistent deployments have different durability. Persistent within one AZ is not multi-AZ failover.",
      },
      {
        service: "FSx for NetApp ONTAP / OpenZFS",
        when: "NetApp multiprotocol/SnapMirror requirements / supported ZFS/NFS workloads.",
        watch:
          "Validate protocol and deployment features rather than treating every FSx service identically.",
      },
    ],
    rules: [
      "ONTAP supports supported NFS, SMB, and iSCSI use cases; ordinary Linux shared NFS may instead fit EFS.",
      "S3 integration with Lustre is managed data association/import/export, not a blanket promise that S3 gains arbitrary filesystem semantics.",
      "Match resilience to the explicitly stated AZ or regional failure scope.",
    ],
    scenario: {
      prompt:
        "A Linux HPC cluster processes a large S3 dataset and needs parallel filesystem access.",
      answer:
        "Consider FSx for Lustre with suitable S3 data repository integration.",
      why: "The workload calls for parallel filesystem throughput rather than a generic object-download path.",
      instead:
        "A Windows SMB application with AD integration points toward FSx for Windows; a simple elastic shared NFS workload may fit EFS.",
    },
    reference:
      "https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html",
  },
  {
    id: "offline-transfer",
    title: "Offline transfer and edge compute",
    domain: "performance",
    guide: "27-Snow-Family.md",
    keywords: [
      "snowball",
      "snowcone",
      "snowmobile",
      "snow family",
      "offline",
      "opshub",
      "limited bandwidth",
    ],
    idea: "If the network cannot move data within the deadline, calculate transfer time and investigate available offline-transfer or edge solutions. Service eligibility is part of that choice.",
    analogy:
      "A truck can carry more data than a narrow pipe, but only if that shipping service is actually available to you.",
    choices: [
      {
        service: "Online transfer",
        when: "A suitable network path can meet the window using supported transfer services.",
        watch:
          "Convert bits to bytes, allow for real utilisation, and include competing traffic.",
      },
      {
        service: "Eligible offline device / partner solution",
        when: "The deadline or disconnected location makes online transport impractical.",
        watch:
          "Snow offerings have changed availability. Do not assume a new customer can order every device listed in older notes.",
      },
    ],
    rules: [
      "At 100 Mbps, 100 TB takes roughly 93 days even at perfect decimal throughput; real transfers take longer.",
      "Separate data-import needs from disconnected edge-compute needs; they do not necessarily require the same hardware.",
      "Keep historical Snowcone/Snowmobile/Snowball questions labelled where their eligibility or capabilities no longer describe a new deployment.",
    ],
    scenario: {
      prompt:
        "A site must transfer hundreds of TB within weeks, but has a shared 100 Mbps link.",
      answer:
        "Calculate the network shortfall, then assess currently available eligible offline or partner-transfer options.",
      why: "The deadline cannot be satisfied by wishing the same link were faster.",
      instead:
        "If bandwidth is sufficient and recurring online synchronisation is required, DataSync and appropriate network connectivity may be the better fit.",
    },
    reference:
      "https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html",
  },
  {
    id: "iac",
    title: "CloudFormation and repeatable infrastructure",
    domain: "resilient",
    guide: "28-CloudFormation.md",
    keywords: [
      "cloudformation",
      "stackset",
      "change set",
      "drift",
      "deletionpolicy",
      "cdk",
      "infrastructure as code",
      "template output",
    ],
    idea: "An infrastructure template describes a repeatable desired stack. Use different safeguards for previewing changes, detecting manual edits, preventing updates, and retaining resources.",
    analogy:
      "A recipe makes the environment repeatable; a change set is the shopping-list difference before cooking the next version.",
    choices: [
      {
        service: "Change sets / drift detection",
        when: "Preview a proposed update / compare supported live resources with their template state.",
        watch:
          "Drift detection does not automatically repair every difference or cover every property.",
      },
      {
        service: "StackSets",
        when: "Deploy a standard template across accounts and Regions.",
        watch:
          "Permissions and deployment targets must be configured; this is not an identity permission ceiling.",
      },
      {
        service: "DeletionPolicy / stack policy",
        when: "Control resource handling on deletion / restrict stack-update changes.",
        watch:
          "Retain, Snapshot, update replacement, and termination protection have distinct scopes.",
      },
    ],
    rules: [
      "Outputs expose values; exports/imports support appropriate cross-stack references. Parameters accept input; mappings provide lookup values.",
      "CDK synthesises infrastructure definitions into CloudFormation templates; application source code is a different concern.",
      "Use templates as the source of truth instead of relying on untracked console edits.",
    ],
    scenario: {
      prompt:
        "Security wants to inspect the resources an infrastructure update will replace before executing it.",
      answer: "Create and review a CloudFormation change set.",
      why: "It previews supported proposed changes before application.",
      instead:
        "Drift detection investigates differences already introduced to live resources.",
    },
    reference:
      "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html",
  },
  {
    id: "governance",
    title: "Organizations, Control Tower, and RAM",
    domain: "secure",
    guide: "29-Organizations-ControlTower.md",
    keywords: [
      "organizations",
      "organisation",
      "control tower",
      "scp",
      "service control",
      "organizational unit",
      "account factory",
      "aws ram",
      "resource access manager",
      "consolidated billing",
    ],
    idea: "Organizations groups accounts and applies supported organisation policies. Control Tower helps establish a governed landing zone. RAM shares supported resources across accounts.",
    analogy:
      "Organizations is the building directory and house rules; Control Tower prepares the offices; RAM lets offices share a meeting room.",
    choices: [
      {
        service: "SCP",
        when: "Restrict the maximum available permissions in member accounts/OUs.",
        watch:
          "It grants nothing and does not restrict the management account. Service-linked roles have important exceptions.",
      },
      {
        service: "Control Tower",
        when: "Set up and govern a multi-account environment with standard account provisioning and controls.",
        watch:
          "Preventive, detective, and proactive controls use different mechanisms; not every control is an SCP.",
      },
      {
        service: "AWS RAM",
        when: "Share supported resources such as subnets or Transit Gateways without copying them.",
        watch:
          "Sharing a resource does not grant every possible action or merge all account identities.",
      },
    ],
    rules: [
      "An administrator in a member account can still be denied by an applicable SCP.",
      "Consolidated billing can share eligible discounts under configured settings; it does not merge the accounts' resources.",
      "Use Identity Center for supported workforce SSO and avoid putting ordinary workloads in the management account.",
    ],
    scenario: {
      prompt:
        "Every new team needs an AWS account with standard logging and governance baselines.",
      answer: "Use Control Tower and suitable Account Factory provisioning.",
      why: "The requirement is repeatable governed account setup, not just a consolidated invoice.",
      instead:
        "Organizations alone addresses account grouping and billing; RAM addresses sharing specific resources.",
    },
    reference:
      "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html",
  },
  {
    id: "catalog",
    title: "Service Catalog and Trusted Advisor",
    domain: "cost",
    guide: "30-ServiceCatalog-TrustedAdvisor.md",
    keywords: [
      "service catalog",
      "portfolio",
      "trusted advisor",
      "approved product",
      "service quota",
    ],
    idea: "One service offers approved infrastructure for users to launch; another recommends improvements to resources already in use.",
    analogy:
      "Service Catalog is a vending machine of approved builds; Trusted Advisor is an adviser pointing out opportunities and risks.",
    choices: [
      {
        service: "Service Catalog",
        when: "Users should self-serve approved products through controlled provisioning.",
        watch:
          "Products, portfolios, constraints, and launch roles govern deployment; it does not replace every organisation policy.",
      },
      {
        service: "Trusted Advisor",
        when: "Review supported best-practice checks and recommendations.",
        watch:
          "Available checks depend on support/service entitlements. Old five-category lists are incomplete; current categories include more areas.",
      },
    ],
    rules: [
      "Recommendations do not imply automatic remediation unless a separate supported workflow is configured.",
      "Use a quota-management workflow for increases; noticing quota pressure and raising a quota are separate actions.",
      "Config evaluates resource state against rules; Inspector finds supported vulnerabilities; neither is simply a replacement name for Trusted Advisor.",
    ],
    scenario: {
      prompt:
        "Teams must launch only approved infrastructure blueprints without receiving broad direct provisioning permissions.",
      answer:
        "Publish Service Catalog products with appropriate constraints and launch roles.",
      why: "It combines self-service provisioning with centrally controlled templates and permissions.",
      instead:
        "An SCP limits actions but does not provide the self-service catalogue of approved configurations.",
    },
    reference:
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html",
  },
  {
    id: "cost-tools",
    title: "Cost tools: see, alert, investigate, rightsize",
    domain: "cost",
    guide: "31-Cost-Management.md",
    keywords: [
      "cost explorer",
      "budgets",
      "budget",
      "cost and usage",
      "cur",
      "cost allocation",
      "compute optimizer",
      "anomaly detection",
      "billing conductor",
      "cost report",
    ],
    idea: "Choose a billing tool by the requested action. A graph, a threshold notification, raw billing records, and resource-sizing advice are different outputs.",
    analogy:
      "Explorer is the bank statement, Budgets the spending alert, billing exports the receipts, and Compute Optimizer the sizing adviser.",
    choices: [
      {
        service: "Cost Explorer / Budgets",
        when: "Analyse and forecast spend / alert on configured cost or usage thresholds.",
        watch:
          "A budget is not a universal hard spending cap. Optional actions have defined scope and prerequisites.",
      },
      {
        service: "Billing Data Exports / CUR + Athena",
        when: "Detailed billing data must be analysed with SQL.",
        watch:
          "Configure exports, access, schema, and updates. A report does not by itself reduce cost.",
      },
      {
        service: "Cost Anomaly Detection / Compute Optimizer",
        when: "Detect unusual spending / obtain supported rightsizing recommendations.",
        watch:
          "Anomaly alerts are not real-time packet-level protection or a guaranteed immediate spending stop.",
      },
    ],
    rules: [
      "Activate appropriate cost-allocation tags. Supported backfill features exist; avoid a blanket claim that history can never be backfilled.",
      "Right-sizing, purchasing discounts, storage lifecycle, and reduced data transfer are separate cost levers.",
      "Optimise only after all stated performance, availability, and security requirements are met.",
    ],
    scenario: {
      prompt:
        "Finance wants a notification when forecast monthly spend exceeds its threshold.",
      answer: "Configure an AWS Budget with forecast-based notifications.",
      why: "The requested action is a threshold alert.",
      instead:
        "Cost Explorer investigates which services caused a change; detailed exports support granular SQL analysis.",
    },
    reference:
      "https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html",
  },
  {
    id: "hybrid-network",
    title: "Direct Connect and VPN",
    domain: "resilient",
    guide: "32-DirectConnect-VPN.md",
    keywords: [
      "direct connect",
      "directconnect",
      "vpn",
      "customer gateway",
      "virtual private gateway",
      "transit vif",
      "private vif",
      "macsec",
      "on-premises network",
    ],
    idea: "A private dedicated network path and an encrypted tunnel solve different requirements. Choose for bandwidth consistency, lead time, resilience, and encryption scope.",
    analogy:
      "VPN is an armoured vehicle on public roads; Direct Connect is a private road that still needs protection for its cargo.",
    choices: [
      {
        service: "Site-to-Site VPN",
        when: "Connect sites using supported encrypted IPsec tunnels, often quickly or as a backup.",
        watch:
          "Public-internet paths have variable performance; tunnel and attachment throughput depends on the supported configuration.",
      },
      {
        service: "Direct Connect",
        when: "Dedicated connectivity and predictable bandwidth fit the requirement.",
        watch:
          "Private does not mean automatically encrypted or highly available. Plan redundant connections/locations and supported encryption.",
      },
      {
        service: "Client VPN",
        when: "Individual remote devices need supported VPN access.",
        watch:
          "A workforce laptop connection is different from connecting an entire datacentre router.",
      },
    ],
    rules: [
      "A VPN over Direct Connect can provide end-to-end IPsec. Supported MACsec encrypts specific link segments and is not identical to end-to-end IPsec.",
      "Private/public/transit VIFs reach different target types. Transit connectivity uses a Direct Connect gateway in the appropriate architecture.",
      "A VPN backup is often cost-effective but must have the capacity, routes, and failover behaviour required for the actual workload.",
    ],
    scenario: {
      prompt:
        "An existing Direct Connect path needs an inexpensive secondary route for a link outage.",
      answer:
        "Consider a Site-to-Site VPN backup with tested routing and sufficient recovery capacity.",
      why: "It adds a distinct path without automatically buying another dedicated circuit.",
      instead:
        "If the backup must provide the same predictable high throughput, redundant Direct Connect connections may be necessary.",
    },
    reference:
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html",
  },
  {
    id: "network-links",
    title: "Peering vs Transit Gateway vs PrivateLink",
    domain: "resilient",
    guide: "33-Transit-Gateway.md",
    keywords: [
      "transit gateway",
      "peering",
      "privatelink",
      "endpoint service",
      "overlapping cidr",
      "transitive",
      "multicast",
      "hub-and-spoke",
    ],
    idea: "Decide whether networks need routed connectivity or consumers only need one service. Network reachability is not the same as exposing a private service endpoint.",
    analogy:
      "Peering is a road between two sites, Transit Gateway a hub, and PrivateLink a service counter that does not join the whole networks.",
    choices: [
      {
        service: "VPC peering",
        when: "A manageable number of non-overlapping VPCs need direct supported routing.",
        watch: "It is non-transitive; A–B and B–C do not create A–C routing.",
      },
      {
        service: "Transit Gateway",
        when: "Many VPCs/sites need hub-and-spoke routing and segmentation.",
        watch:
          "Attachments, route-table associations/propagation, and processing charges matter. Connectivity is not automatic permission for every flow.",
      },
      {
        service: "PrivateLink",
        when: "Consumers need private access to a supported provider service without broad network routing.",
        watch:
          "Suitable endpoint-service designs can tolerate overlapping CIDRs. Check supported service/network load-balancer patterns.",
      },
    ],
    rules: [
      "Use RAM to share a supported Transit Gateway across accounts; route tables can isolate prod/dev while sharing on-premises access.",
      "Transit Gateway multicast has specific supported resource/attachment constraints; do not assume every attached network can use it.",
      "Overlapping CIDRs prevent ordinary peering/routed connectivity; a service endpoint is a different model, not a way to route arbitrary overlapping networks.",
    ],
    scenario: {
      prompt:
        "A SaaS provider exposes one API to many customer VPCs, some with overlapping address ranges.",
      answer: "Use a suitable PrivateLink endpoint-service architecture.",
      why: "Customers access the service through endpoints without merging the provider's entire network.",
      instead:
        "Transit Gateway is appropriate when many non-overlapping networks need routed, transitive connectivity.",
    },
    reference:
      "https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service-overview.html",
  },
  {
    id: "architecture",
    title: "Well-Architected and question qualifiers",
    domain: "cost",
    guide: "34-Well-Architected.md",
    keywords: [
      "well-architected",
      "well architected",
      "sustainability",
      "least operational",
      "most cost-effective",
      "architecture tradeoff",
    ],
    idea: "The question's objective breaks ties only after all mandatory requirements are satisfied. 'Works' and 'best under these constraints' are different conclusions.",
    analogy:
      "Choose a vehicle that can carry the load and finish the journey, then optimise fuel cost—not the cheapest vehicle that cannot do the job.",
    choices: [
      {
        service: "Cost optimisation",
        when: "Select the least total cost among solutions meeting all requirements.",
        watch:
          "Include transfer, requests, idle capacity, retrieval, and management—not only the headline storage rate.",
      },
      {
        service: "Operational overhead",
        when: "Prefer supported managed capabilities when they satisfy the scenario.",
        watch:
          "Serverless is not an automatic winner if its limits or compatibility fail a requirement.",
      },
      {
        service: "Reliability / performance / security",
        when: "The objective explicitly emphasises failure recovery, speed, or protection.",
        watch:
          "A performant system is not automatically secure, and a multi-AZ system is not automatically multi-region.",
      },
    ],
    rules: [
      "The six pillars are operational excellence, security, reliability, performance efficiency, cost optimisation, and sustainability.",
      "Extract each hard requirement, eliminate violating options, then apply the requested objective to the survivors.",
      "Avoid absolute keyword shortcuts. Ask which deployment type, failure scope, protocol, and lifecycle the question actually states.",
    ],
    scenario: {
      prompt:
        "Two designs meet the same SLA. One requires self-managed workers; the other uses a supported managed service. The question asks for least operational overhead.",
      answer: "Prefer the managed design if it meets every stated requirement.",
      why: "The objective is management effort, not an unrelated preference for maximum control.",
      instead:
        "A custom OS, unsupported protocol, or incompatible service limit can make the self-managed design necessary.",
    },
    reference:
      "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html",
  },
  {
    id: "dr",
    title: "Disaster recovery: data loss vs downtime",
    domain: "resilient",
    guide: "35-Disaster-Recovery.md",
    keywords: [
      "disaster",
      "rpo",
      "rto",
      "recovery",
      "pilot light",
      "warm standby",
      "active-active",
      "backup",
      "failover",
      "drs",
    ],
    idea: "RPO measures acceptable data loss in time; RTO measures acceptable downtime. Choose and test a recovery design whose data, infrastructure, and application steps meet both.",
    analogy:
      "A backup is a stored recipe; pilot light keeps essential ingredients ready; warm standby has a small kitchen running; active-active serves from multiple kitchens.",
    choices: [
      {
        service: "Backup and restore",
        when: "Low standby cost matters and tested restore time meets the objective.",
        watch:
          "Backup frequency affects RPO; data size, quotas, infrastructure creation, and validation affect RTO.",
      },
      {
        service: "Pilot light / warm standby",
        when: "Keep core services ready / keep a reduced complete environment running.",
        watch:
          "Recovery times depend on scaling and testing. A generic '10 minutes means warm standby' rule is not a guarantee.",
      },
      {
        service: "Multi-site active-active",
        when: "Serving from multiple sites is justified by stringent resilience needs.",
        watch:
          "Replication conflicts, routing, consistency, dependencies, and detection still prevent a blanket zero-data-loss/zero-downtime promise.",
      },
      {
        service: "AWS Backup / Elastic Disaster Recovery",
        when: "Central backup policies / supported continuous server replication and recovery.",
        watch:
          "Backups protect historical states; replication can also replicate corruption. They are complementary.",
      },
    ],
    rules: [
      "AZ failure and Region failure require different redundancy scopes. Multi-AZ alone does not solve losing the Region.",
      "PITR restores a historical state; Global Tables replicate ongoing changes. Recovery from accidental deletion and a regional outage are different scenarios.",
      "Test restoration and application cutover. A stated service replication lag alone is not the end-to-end RTO.",
    ],
    scenario: {
      prompt:
        "The database is continuously replicated, but application servers are launched only when a disaster is declared.",
      answer: "This is a pilot-light pattern.",
      why: "Essential data/core services remain ready while the full application tier is not continuously running.",
      instead:
        "A reduced complete application already serving or ready to serve describes warm standby; historical backups alone describe backup/restore.",
    },
    reference:
      "https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html",
  },
  {
    id: "exam-technique",
    title: "Exam technique: constraints before keywords",
    domain: "resilient",
    guide: "36-Exam-Traps-KeyPatterns.md",
    keywords: [
      "exam technique",
      "timing",
      "eliminat",
      "qualifier",
      "select two",
    ],
    idea: "Turn a long story into a short checklist, eliminate unsupported choices, and use the objective to distinguish the remaining valid designs.",
    analogy:
      "You are checking a proposal against a contract, not playing service-name bingo.",
    choices: [
      {
        service: "Requirement checklist",
        when: "A scenario includes several needs joined by 'and', 'also', or exact limits.",
        watch: "A choice satisfying only one requirement is still incomplete.",
      },
      {
        service: "Compare the differing clause",
        when: "Two long options are nearly identical.",
        watch:
          "One word such as automatically, directly, synchronous, or multi-region can change the whole answer.",
      },
      {
        service: "Answer, flag, move",
        when: "You are spending too long without gaining new evidence.",
        watch:
          "Reserve time to revisit. There is no penalty for an incorrect guess, so do not intentionally leave blanks.",
      },
    ],
    rules: [
      "A 65-question, 130-minute mock averages two minutes per question. A useful first-pass target is around 100–110 minutes, leaving review time; adapt to your actual pace.",
      "For multi-response questions, each chosen option must contribute to a valid complete solution. Practice uses exact-set grading.",
      "Review uncertain correct answers as well as errors. Repeated-question accuracy is not fresh-question evidence or an AWS scaled score.",
    ],
    scenario: {
      prompt:
        "You recognise two services that could solve the problem, but the question asks for least operational overhead.",
      answer:
        "Check hard requirements first, then compare the management work of the valid candidates.",
      why: "Recognising a keyword is only the start; the requested tradeoff decides the best answer.",
      instead:
        "If the same question asked for full host control, a more self-managed service could be the correct choice.",
    },
    reference:
      "https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html",
  },
  {
    id: "gap-services",
    title: "Migration, integration, and smaller services",
    domain: "performance",
    guide: "37-GapFill-Services.md",
    keywords: [
      "migration",
      "dms",
      "schema conversion",
      "mgn",
      "amazon mq",
      "rabbitmq",
      "activemq",
      "comprehend",
      "textract",
      "transcribe",
      "rekognition",
      "polly",
      "glue",
      "lake formation",
      "emr",
      "msk",
      "appsync",
      "batch",
      "artifact",
      "acm",
      "systems manager",
    ],
    idea: "Recognise the operation and compatibility requirement. Managed migration, broker compatibility, text extraction, language analysis, and data cataloguing are different tasks.",
    analogy:
      "A moving company, translator, scanner, and librarian all handle information but are not substitutes for each other.",
    choices: [
      {
        service: "MGN / DMS + schema conversion",
        when: "Rehost supported servers / migrate supported databases, converting schema when needed.",
        watch:
          "Validate source/target support and conversion gaps. Database migration is not just copying arbitrary server files.",
      },
      {
        service: "Amazon MQ / MSK",
        when: "Supported traditional broker protocols / Apache Kafka compatibility.",
        watch:
          "A new queueing application may instead suit SQS; compatibility with an existing broker stack is an explicit requirement.",
      },
      {
        service: "Textract / Comprehend / Transcribe",
        when: "Extract document fields / analyse language meaning or sentiment / turn speech into text.",
        watch:
          "If a transcript already exists, speech-to-text is not the missing step.",
      },
      {
        service: "Glue / Lake Formation / EMR",
        when: "Supported ETL/catalogue / data-lake governance / supported big-data frameworks.",
        watch:
          "Permissions, data formats, and compute choices still determine whether the whole solution works.",
      },
    ],
    rules: [
      "ACM supports exportable public certificates under supported paid configurations; the old 'public ACM certificates can never be exported' rule is outdated.",
      "SSM Session Manager, Run Command, and Patch Manager address interactive access, fleet commands, and patching respectively; logging depends on configuration and session type.",
      "Pinpoint campaigns/journeys reached end of support on October 30, 2026. Relevant messaging APIs continue under AWS End User Messaging; do not transplant an old journey recommendation into a new design.",
    ],
    scenario: {
      prompt:
        "Call transcripts are already JSON in S3. Extract sentiment and visualise it with minimal custom machine-learning work.",
      answer:
        "Use suitable Comprehend sentiment analysis, then a supported analytics/search and dashboard pipeline.",
      why: "The missing capability is language analysis, not transcription or document OCR.",
      instead:
        "Textract extracts structured information from documents; Transcribe is appropriate when the source is still audio.",
    },
    reference: "https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html",
  },
];
