"""Independent November editorial decisions. Letters refer to the captured option order.

No screenshot selections are used. Explicit merges retain the existing corrected study
variant and its editorial notes; changed statements are never used to remap saved answers.
"""
REVIEWS = {}
HOLDS = {}
MERGES = {1: "q-32e0bb1ad3", 7: "q-286412cfe6", 12: "q-b91a4e4dba", 66: "q-9c775971f5", 82: "q-a3ec79a777", 96: "q-cd31f4874c", 114: "q-c2e1099cc3"}
# Explicit continuation sources, whose truncated text is superseded by the complete capture.
CONTINUATIONS = {164: 165, 185: 186}
MERGES.update({230: "q-4dc4cf4996", 278: "q-e96bab5408"})
REASONING = {
    2: {"ask":"Identify the properties of Standard-IA, not the cheapest class for every possible archive.", "requirements":["Infrequent object access", "Immediate retrieval when requested"], "why":"Standard-IA stays online with millisecond access while charging differently for cold storage and retrieval.", "alternative":"Intelligent-Tiering automatically changes supported access tiers; Standard-IA does not.", "alternativeWhen":"Choose Intelligent-Tiering when access patterns are unknown or changing and its monitoring/tiering model fits."},
    128: {"ask":"Keep legacy response formats working without changing the upgraded backend.", "requirements":["API Gateway REST API", "Transform response format", "No backend modification"], "why":"A suitable integration response mapping template translates the backend body into the old client format.", "alternative":"Caching keeps a copy of a response but does not change its schema.", "alternativeWhen":"Choose caching when repeated identical reads overload a backend and cached responses can satisfy freshness/authorisation requirements."},
    143: {"ask":"Give an EC2 application a private path to Secrets Manager.", "requirements":["Access Secrets Manager", "Avoid the public service path", "Keep appropriate IAM/decryption controls"], "why":"An interface endpoint places private service-access ENIs in the VPC and supports endpoint policies and security groups.", "alternative":"A gateway endpoint is tempting because it is a private AWS endpoint, but Secrets Manager does not use that endpoint type.", "alternativeWhen":"Use a gateway endpoint for suitable VPC-local S3 or DynamoDB access."},
    150: {"ask":"Read existing quiz text aloud.", "requirements":["Input is already plain text", "Output must be spoken audio"], "why":"Polly performs text-to-speech without an OCR or speech-recognition stage.", "alternative":"Textract extracts text from documents; it does not turn the resulting text into speech.", "alternativeWhen":"Use Textract when the input is still a scanned form, invoice, or another supported document."},
    171: {"ask":"Absorb a burst of writes without buying a larger database immediately.", "requirements":["Writes may complete asynchronously", "Database drain rate is constrained", "Preserve accepted work"], "why":"A durable SQS backlog lets workers execute writes at a sustainable rate and retry failures.", "alternative":"Read replicas address read demand, not write bursts on the primary; replacing the database is also a much larger change.", "alternativeWhen":"A read replica is useful when appropriate reporting/read queries are overloading the primary."},
    196: {"ask":"Improve product text search rather than build an analytics dashboard.", "requirements":["Full-text matching", "Synonyms", "Typo-tolerant queries"], "why":"OpenSearch has appropriate indexing, analyzers, and query capabilities for the requested search behaviour.", "alternative":"QuickSight can visualise analysed data, but it is not the application's full-text search index.", "alternativeWhen":"Choose QuickSight for business dashboards and supported interactive visualisation of analytical datasets."},
    235: {"ask":"Force administrative RDP connections to the production instances through the bastion.", "requirements":["Protect the destination servers", "Permit RDP only from the bastion"], "why":"A target-server inbound security-group rule naming the bastion's group enforces the source restriction at the destination.", "alternative":"Restricting who enters the bastion is useful but does not eliminate another direct path into the production servers.", "alternativeWhen":"A corporate-IP restriction on the bastion is an additional perimeter control; combine it with target rules when a bastion is required."},
    236: {"ask":"Diagnose a network timeout despite an associated S3 gateway endpoint.", "requirements":["Same-Region S3 path exists", "Request times out rather than returning AccessDenied", "Consider both traffic directions"], "why":"Security-group egress can block requests; stateless NACLs can separately block their return traffic.", "alternative":"Missing S3 permissions are plausible for AccessDenied, but do not normally explain this chosen network-timeout symptom.", "alternativeWhen":"Investigate identity, endpoint, bucket, and KMS policies when the network reaches the service and an authorisation denial is returned."},
}

def a(index, answer, doc, takeaway, *explanations, note="", prompt=None, options=None, domain=None):
    assert answer and all(c in "ABCDEF" for c in answer), (index, answer)
    REVIEWS[index] = dict(correct=[ord(c)-65 for c in answer], docs=[doc], takeaway=takeaway,
                          explanations=list(explanations), note=note, prompt=prompt, options=options, domain=domain)

def h(index, doc, reason):
    HOLDS[index] = {"docs":[doc], "note":reason}

a(2,"AC","s3","Standard-IA combines infrequent access with millisecond retrieval; it does not automatically choose access tiers.",
  "Standard-IA is an online storage class with low-latency access when the objects are needed.",
  "For genuine archival access, compare Glacier classes and retrieval deadlines; this is not Standard-IA's defining property.",
  "Infrequently accessed data with immediate retrieval is the intended Standard-IA access pattern.",
  "Automatic access-tier selection describes Intelligent-Tiering, not Standard-IA.",
  "Standard-IA does not deliberately provide high latency and poor throughput.",
  note="Editorial clarification: storage classes apply to objects, not a bucket-wide conversion of existing contents. Minimum-duration, retrieval, and object-size charges must also be considered.")
a(9,"C","video","Ingest camera video with Kinesis Video Streams, analyse supported imagery with Rekognition, and notify through an application workflow.",
  "Prometheus collects metrics; Fraud Detector is not a camera-video identity recognition engine.",
  "A media transcoder and enterprise text search do not provide the requested visual identity analysis.",
  "This is the only offered video-ingestion and visual-analysis combination; add application logic and configured SNS SMS delivery for alerts.",
  "Control Tower governs accounts; it does not inspect a device's face-detection output and send these security alerts.",
  note="The source abbreviates the full workflow: frame extraction or supported stream analysis, enrolled-reference matching, an unknown-person rule, and notification logic are still required. Recognising a face alone does not establish authorisation.")
a(10,"A","rds","A connection pool addresses too many database connections; increasing incoming concurrency can worsen the problem.",
  "RDS Proxy pools and reuses supported MySQL database connections, reducing repeated connection creation.",
  "Raising API request limits can increase database pressure rather than reuse existing connections.",
  "More function memory can improve CPU performance but does not provide a shared database connection pool.",
  "Higher concurrency permits more simultaneous functions and can create still more database connections.")
a(13,"BC","sse","SSE-S3 or client-side encryption can protect S3 object data at rest; HTTPS alone only protects transit.",
  "EBS snapshots protect EBS block data; they are not a way to encrypt arbitrary backup objects already stored in an S3 bucket.",
  "SSE-S3 encrypts S3 object data using AES-256 with service-managed keys.",
  "Encrypting the payload locally before upload is a valid client-side encryption design with customer key-management responsibilities.",
  "SSE-S3 uses AES-256, not the stated AES-128 server-side setting.",
  "Moving the data to EBS changes the required storage service instead of encrypting the specified S3 backups.",
  note="All new S3 uploads receive baseline server-side encryption by default. This question compares encryption approaches, not the complete set of controls needed for a regulated workload.")
a(16,"CE","sqs","SQS buffers work and SWF coordinates supported workers; both can involve on-premises and AWS-hosted code.",
  "VPC peering connects VPCs, not an on-premises server fleet directly, and does not itself decouple application work.",
  "DynamoDB stores data but is not by itself the queue or workflow service described by these choices.",
  "On-premises and EC2 producers/consumers can use SQS through suitable network and IAM access.",
  "A relational database is not by itself a managed work queue or workflow coordinator.",
  "SWF can coordinate application workers running in AWS or on-premises through its APIs.",
  note="This is a historical service-recognition comparison. For a new orchestrated workflow, also assess current Step Functions capabilities; network connectivity and permissions are required in either location.")
h(17,"snow","Historical answer is Snowball Edge, but it is no longer available to new customers and the source establishes no eligibility. Snowmobile is also obsolete. Multipart upload cannot overcome the stated bandwidth; assess current physical-transfer/partner options instead.")
a(18,"D","waf","Filter SQL injection and XSS at the HTTP layer using WAF on the ALB.",
  "Blocking observed addresses does not inspect HTTP attack content and attackers can change source addresses.",
  "GuardDuty detects supported threat activity; it is not an inline SQL-injection/XSS request filter.",
  "Firewall Manager can centrally distribute WAF policies, but direct WAF configuration is the appropriate offered control for this single application.",
  "WAF web ACL rules on a supported ALB can inspect and block matching SQL injection and XSS requests.")
a(39,"D","routing","Geoproximity bias changes the geographic catchment area of regional resources.",
  "Geolocation applies location-based rules rather than expanding a resource's catchment area with bias.",
  "Latency routing chooses measured latency rather than a configurable geographic-area expansion.",
  "Weighted routing changes assigned proportions but is not a geographic catchment-area bias rule.",
  "Geoproximity lets the architect bias a resource to receive traffic from a larger geographic area.",
  prompt="A messaging application runs in ap-northeast-1 and ap-southeast-2. The architect wants to expand the geographic catchment area of the ap-northeast-1 resource, drawing more traffic from locations such as the Philippines and northern India by adjusting a geographic bias. Which Route 53 routing policy supports this?",
  note="Editorial study variant: geographic catchment and bias are explicit because the original 'larger portion' wording could also suggest weighted routing.")
a(46,"C","dms","DMS full load plus CDC handles an initial database copy and ongoing changes; configure source TLS with the right certificate.",
  "Full load alone does not capture later changes, and Network Firewall is not the mechanism for adding a DMS endpoint certificate.",
  "SCT converts supported schema/code; MGN replicates servers rather than emitting a MySQL change stream as S3 CSV files.",
  "A full-load-and-CDC task covers both phases; a suitable CA and endpoint SSL settings secure the source connection.",
  "An offline device and filesystem synchronisation do not provide the requested ongoing native MySQL change capture.",
  note="Configure an appropriate S3 target endpoint/format, IAM permissions, and encryption separately. RDS Proxy is not part of the database-to-S3 ingestion path.")
a(51,"D","sse","Explicit SSE-S3 requests use x-amz-server-side-encryption with the value AES256.",
  "The customer-key header belongs to SSE-C, where the requester supplies encryption key material.",
  "The customer-key-MD5 header verifies an SSE-C customer key, not an SSE-S3 selection.",
  "The customer-algorithm header is part of SSE-C rather than the SSE-S3 request field.",
  "Set x-amz-server-side-encryption to AES256 to explicitly request SSE-S3.",
  prompt="An application explicitly requests SSE-S3 encryption for an S3 object upload, using Amazon S3-managed AES-256 keys. Which request header carries the AES256 value?",
  note="Editorial clarification: an explicit request is specified. A header is not required merely to obtain S3's default encryption for a new upload.")
a(54,"A","costtags","Activate department cost-allocation tags to group billing by department.",
  "Department tags provide the grouping dimension; activating them makes the relevant tags available in billing analysis.",
  "A resource filter without a maintained department dimension does not reliably group all departmental usage.",
  "Budget actions respond to thresholds; they do not activate department tags for cost attribution.",
  "A service-only report does not distinguish departments sharing the same AWS service.")
a(56,"D","gateway","Tape Gateway can replace physical tape workflows and archive virtual tapes into a suitable low-cost archive tier.",
  "The option does not identify the cheapest long-term archive tier and compresses the virtual-tape lifecycle into a direct backup statement.",
  "Snowball is not a direct-to-Glacier tape-backup integration and has current customer-eligibility restrictions.",
  "S3 lifecycle storage can archive objects but alone does not preserve the existing tape-library interface.",
  "A suitable Tape Gateway workflow preserves the tape interface and can archive virtual tapes in Deep Archive for long retention.",
  note="The intended Storage Gateway subtype is Tape Gateway. Recent tapes and archived tapes have different access/restore behaviour; ten-year retention still requires an appropriate backup/retention policy.")
a(64,"C","cloudfront","Store durable report objects in S3 and distribute supported downloads through CloudFront.",
  "Glacier restore delays are not a general online-report design, and ElastiCache is not a global CDN.",
  "Redshift is an analytics warehouse, not the natural durable store for generated report files.",
  "S3 provides scalable durable object storage, while CloudFront caches and delivers content nearer global viewers.",
  "Instance-store data is ephemeral, and ElastiCache does not provide global CDN delivery.")
a(65,"D","eks","Kubernetes compatibility and portability distinguish EKS from AWS-native ECS orchestration.",
  "ECR stores container images; it does not orchestrate application containers on worker nodes.",
  "ECS with Fargate removes server management but does not provide the requested Kubernetes/open-source orchestration interface.",
  "ECS on EC2 changes the compute layer but remains ECS rather than Kubernetes.",
  "EKS provides managed Kubernetes, allowing supported existing Kubernetes manifests and tooling to be reused.")
h(70,"auroraha","The source uses obsolete MySQL 5.6 and asks for a cross-region replication latency below a fixed second without stating an Aurora Global Database or other sufficient architecture. Ordinary cross-region replica lag is workload-dependent; no offered statement guarantees the claimed latency.")
a(92,"A","cfnfull","A CloudFormation template must declare Resources; Parameters and Outputs alone do not define infrastructure.",
  "Resources declares the stack's infrastructure and is the required missing section in this clarified example.",
  "Parameters is a valid optional CloudFormation section for stack inputs.",
  "Conditions is optional and only needed when conditional logic is required.",
  "The supported template format version is 2010-09-09, not the proposed 2017 date.",
  prompt="A CloudFormation template declares valid Parameters and Outputs sections, but declares no Resources section. The engineer expects it to provision an EC2 application. Why will this template fail to define the intended deployable stack?",
  note="Editorial study variant replaces the screenshot's poorly extracted JSON with an explicit section-level description; it tests the missing Resources section rather than OCR syntax artefacts.")
a(111,"CD","orgbilling","Separate AWS accounts preserve division autonomy; cross-account roles and consolidated billing support central oversight.",
  "Best-practice recommendations and tag editing alone do not establish separate division account boundaries and central billing.",
  "AZs are infrastructure failure domains, not division-owned accounts, and Global Accelerator does not merge AZ administration.",
  "Appropriately scoped cross-account administrative roles let authorised corporate IT staff oversee member accounts.",
  "Organizations consolidated billing gives the management account cost oversight while each member account remains separate.",
  "Separate VPCs inside one account do not provide the requested distinct account-level administration and billing structure.")
a(115,"D","vpc","RDP uses TCP 3389; allow it only from the required administrator source.",
  "Restarting does not add the missing network permission and is not a targeted fix.",
  "Port 22 is the conventional SSH port, not the Windows RDP listener.",
  "Replacing the instance without repairing its security-group policy can reproduce the same problem.",
  "Allowing the company's source address on TCP 3389 supplies the relevant RDP network permission.",
  note="The OS must also run the RDP service and permit it through its host firewall; the public addressing and routes are already given.")
a(116,"D","kinesis","Default Kinesis Data Streams retention is 24 hours; a three-day delayed consumer must extend retention.",
  "There is no evidence of manual S3 deletion; the observed one-day window matches stream retention.",
  "A permission failure would not normally explain successful retention of only the latest day's stream records.",
  "S3 data loss is not the supported explanation for records that expired before the consumer read them.",
  "A stream with default 24-hour retention no longer has records from two or three days earlier.")
a(118,"AB","efa","Enhanced networking improves packet processing and network latency, not a dedicated hybrid circuit.",
  "Enhanced networking can deliver higher packet-per-second performance through supported networking capabilities.",
  "It reduces network overhead and can provide consistently lower inter-instance latency on supported instances.",
  "Low packet-processing capability is not the performance benefit enhanced networking is selected to obtain.",
  "A dedicated on-premises connection is a Direct Connect concern, not an EC2 enhanced-networking feature.",
  "Higher latency is the opposite of the intended networking-performance improvement.")
a(119,"C","nat","Use public NAT gateways for private IPv4 instances that initiate internet downloads.",
  "A service endpoint does not provide general internet access to arbitrary operating-system patch repositories.",
  "A NAT instance requires capacity, patching, and a separate HA design managed by the customer.",
  "Managed public NAT gateways support outbound IPv4 access and return traffic without permitting unsolicited internet initiation.",
  "An egress-only internet gateway is for supported IPv6 traffic, not these IPv4-only instances.",
  note="For zonal NAT gateways, use a gateway per required AZ and suitable public-subnet/IGW routes. A single zonal gateway is not a complete multi-AZ HA design.")
a(120,"A","kinesis","Increase provisioned Kinesis shard capacity when measured stream capacity is the bottleneck.",
  "For a provisioned stream, UpdateShardCount can increase shard count and aggregate supported ingestion/consumption capacity.",
  "An EC2-style step scaling policy is not a direct Kinesis stream configuration option by itself.",
  "Merging shards reduces provisioned shard capacity rather than relieving an aggregate-capacity shortfall.",
  "Firehose changes the consumption/delivery model and does not preserve this real-time Lambda processing architecture automatically.",
  note="Interpret this as a provisioned-capacity question. Confirm hot partition keys, consumer limits, and Lambda bottlenecks; adding shards alone cannot fix every performance problem.")
a(121,"B","ebs","Select storage-optimised EC2 when large local datasets and storage throughput dominate.",
  "Compute-optimised instances target CPU demand rather than the stated large sequential local-storage workload.",
  "Storage-optimised families provide local storage options designed for high storage capacity and throughput/IOPS workloads.",
  "Memory-optimised instances target RAM-intensive workloads rather than this local-disk requirement.",
  "General-purpose instances balance resources but do not specifically optimise the stated dominant local-storage demand.")
a(122,"A","cache","Memcached fits this multithreaded distributed-cache requirement; discovery is not data replication.",
  "A supported Memcached cluster provides multithreaded cache access, node replacement, and client Auto Discovery of cluster membership.",
  "Sticky sessions keep a client on a target but do not supply a shared distributed session store.",
  "RDS Proxy pools relational connections; it is not the sub-millisecond distributed cache described here.",
  "Redis Global Datastore targets cross-region Redis replication rather than this explicit multithreaded Memcached/Auto Discovery pattern.",
  note="Node replacement does not recover lost Memcached entries. This answer assumes disposable/reconstructable session data as in the source; a requirement to preserve sessions through node loss would need a different design.")
a(123,"B","versioning","Keep previous object contents using versioning or distinct versioned keys; invalidation only changes cached availability.",
  "Invalidating a CloudFront object expires a cached copy; it does not preserve a previous object in S3.",
  "Versioned objects preserve previous content, with new keys also providing a clean CloudFront cache-versioning strategy.",
  "Cache directives affect caching and freshness but do not retain overwritten object data.",
  "A zero TTL can force freshness checks but cannot recover previous S3 content after an overwrite.",
  note="S3 Versioning retains object versions under one key; versioned filenames create distinct keys. For CloudFront freshness, explicitly request the desired key or version.")
a(124,"A","efs","Regional EFS provides shared POSIX/NFS access across multiple AZs.",
  "Regional EFS supports concurrent Linux file access through mount targets across AZs with regional file durability.",
  "S3 is an object API, not the requested native POSIX shared filesystem.",
  "EBS is AZ-scoped block storage and does not provide an ordinary multi-AZ shared filesystem.",
  "ElastiCache is an in-memory data store, not the requested durable POSIX file service.")
a(125,"D","cloudwatch","Install and configure a host logging agent to send EC2 application logs to CloudWatch Logs.",
  "CloudTrail integrity validation checks CloudTrail log files rather than forwarding arbitrary EC2 application logs.",
  "Transfer Family provides managed transfer protocols, not host log collection into CloudWatch Logs.",
  "The CloudTrail Processing Library processes CloudTrail records rather than tailing this instance's application log files.",
  "A configured CloudWatch logging agent can collect local files and publish them to log streams with the required IAM permissions.",
  note="Prefer the current unified CloudWatch agent over the legacy Logs-only agent named by the source.")
h(126,"gateway","The intended file-gateway local-cache answer does not guarantee that a historical backup from exactly 48 hours ago remains locally cached: cache entries are evictable and require version/backup management. The other options also omit the required historical-state and immediate-local-access guarantee. Cache sizing alone is not a retention policy.")
h(127,"kinesis","The intended historical Pinpoint-journey answer depends on a service feature whose support ended October 30, 2026. The other options do not provide the complete two-way SMS, streaming analysis, and one-year retention design. Relevant messaging APIs continue under AWS End User Messaging, but the offered journey design is obsolete.")
a(128,"B","apigw","Mapping templates transform a supported REST integration response for legacy clients.",
  "Caching reuses a response and does not translate an incompatible response schema.",
  "Integration response mapping templates can transform the backend payload into the format required by legacy clients.",
  "Gateway responses customise gateway-generated responses such as errors, not arbitrary successful backend payload transformation.",
  "Method response models describe response structure but do not themselves rewrite the body.")
a(129,"A","ecs","An ECS task definition is a JSON blueprint describing the containers and task settings.",
  "The task definition specifies containers, images, resources, networking-related settings, and supported IAM role references.",
  "This vague program description misses the specific multi-container task blueprint and its runtime settings.",
  "A task definition is configuration data, not a managed service that creates ECS clusters.",
  "IAM policies govern permissions; they are not the container application blueprint called a task definition.")
a(130,"B","redshift","Redshift data sharing can expose authorised live datasets across accounts without duplicating the data.",
  "An ETL export/load pipeline duplicates data and adds the operational process the requirement excludes.",
  "An authorised Redshift datashare lets supported consumer warehouses access shared data without building a copied dataset.",
  "S3 export and cross-account access adds a separate copy and export lifecycle.",
  "Moving warehouse datasets to DynamoDB changes the data model and creates another copy.",
  note="Configure producer/consumer authorisation and supported encrypted warehouse/serverless settings. Consumer compute charges still apply.")
a(131,"C","ram","Use RAM to share supported common resources directly with the intended member accounts.",
  "Some services support resource-policy sharing, but RAM is the central sharing mechanism for the supported infrastructure resources described.",
  "Sharing only with the management account does not provide the requested member-account access.",
  "RAM resource shares let approved member accounts use supported common resources without independently duplicating them.",
  "RAM shares are not automatically re-shared transitively through the management account.")
a(133,"D","as","OldestLaunchTemplate favours instances using older launch-template configurations when scale-in occurs.",
  "Billing-hour proximity does not specifically target outdated launch-template configurations.",
  "The oldest instance is not necessarily using the oldest launch template or template version.",
  "AllocationStrategy preserves supported allocation choices rather than specifically retiring the oldest launch template.",
  "OldestLaunchTemplate preferentially selects instances with old launch-template configurations within the termination-policy process.",
  note="A termination policy selects instances during scale-in; it does not proactively roll an entire fleet. Update the ASG template and use an instance refresh for a controlled fleet replacement.")
h(134,"auroraha","Aurora Global Database is a relevant cross-region recovery architecture, but the offered answer claims automatic regional takeover without specifying an orchestrated detection/failover/application workflow. Built-in in-region Multi-AZ failover is not global automatic failover, and sub-minute end-to-end recovery is not guaranteed by this source.")
a(135,"B","waf","Scope a WAF rate-based rule to the expensive URI paths rather than throttling every resource.",
  "A blanket rate rule can also limit lightweight resources that the requirement wants unrestricted.",
  "A rate-based rule with a URI scope-down statement counts and limits only the selected expensive endpoints.",
  "IP reputation addresses known bad sources, not every legitimate client issuing too many expensive requests.",
  "Managed exploit rules do not directly implement the requested endpoint-specific request-rate policy.")
a(136,"C","routing","Use separate primary and secondary failover records with health checks appropriate to each target.",
  "One failover record does not represent both the primary ALB and independent on-premises secondary target.",
  "A single alias cannot express both failover targets and attach distinct target-specific health behaviour.",
  "The primary ALB alias can evaluate target health, while a secondary address record uses an appropriate reachable endpoint health check.",
  "This reverses the required primary AWS and secondary on-premises roles.")
a(137,"C","datasync","DataSync can perform managed recurring transfers between supported EFS locations across Regions.",
  "Staging through S3 adds copies and transfer steps when a supported direct EFS transfer can be configured.",
  "Self-managed tools and VPN operations introduce more configuration and maintenance than the managed transfer option.",
  "DataSync supports scheduled transfers between suitable EFS locations with managed encryption and network configuration.",
  "Shipping devices is not an appropriate recurring online EFS-to-EFS transfer design and has availability restrictions.",
  note="Configure supported private network access, security groups, endpoint access, encryption, and scheduling. DataSync is a copy/synchronisation service, not a transparent cross-region shared filesystem.")
a(138,"A","cfnfull","A custom resource can resolve an AMI dynamically during CloudFormation deployment.",
  "A Lambda-backed custom resource can look up the appropriate region/type AMI and return its ID to the template.",
  "Manual template edits retain the repetitive maintenance the requirement asks to remove.",
  "SNS notifications alone do not resolve and inject an AMI into the resource definition.",
  "Adding SQS does not itself perform the required template-time AMI lookup.",
  note="This is the best of the listed options. For predefined static tables, Mappings is simpler; suitable SSM public/custom parameters can avoid custom lookup code when available.")
a(139,"B","scp","An SCP can deny new creation actions for member accounts without removing existing network resources.",
  "SCPs do not restrict identities in the Organizations management account.",
  "Denying the relevant creation actions restricts new resources in member accounts while leaving existing paths in place.",
  "Blocking all internet access exceeds the requirement and disrupts existing working connectivity.",
  "Restricting access to existing gateways conflicts with the requirement to preserve current internet access.")
a(140,"B","publicip","Hibernation preserves a supported instance's own prepared RAM state on its encrypted root EBS volume.",
  "An AMI preserves disk configuration but does not preserve the live in-memory state of an initialised application.",
  "A prepared hibernated backup can resume its own memory state, reducing application reinitialisation time on supported instances.",
  "An ordinary stop loses RAM state and requires normal application initialisation when the instance starts.",
  "Manually writing arbitrary RAM data to a volume and rebooting is not equivalent to supported EC2 hibernation.",
  note="Hibernation does not automatically copy the primary's current state into a different backup instance. Prepare that backup and synchronise application data separately; check instance/OS/encrypted-root requirements.")
a(141,"A","vpn","Transit Gateway can use ECMP across supported dynamic-routing VPN paths for aggregate throughput.",
  "A suitable Transit Gateway with multiple BGP VPN paths and ECMP can distribute independent flows across available tunnels.",
  "A virtual private gateway does not provide this equivalent ECMP aggregation across VPN tunnels.",
  "Creating multiple independent TGWs is not the single ECMP routing design described by the valid option.",
  "Multiple virtual private gateways do not automatically combine their tunnel throughput into this supported ECMP design.",
  note="Aggregate throughput differs from one-flow throughput. Avoid overlapping routes, confirm BGP/ECMP support, and size the on-premises device accordingly.")
a(142,"A","nat","For zonal NAT, keep high-volume outbound traffic on a public NAT gateway in its own AZ.",
  "An AZ-local public NAT gateway with suitable routes avoids the unnecessary cross-AZ leg for that workload.",
  "A public NAT gateway needs a public subnet path to an internet gateway to provide internet egress.",
  "A private NAT gateway does not provide the required internet-gateway translation path.",
  "Placing a private NAT gateway in a public subnet does not turn it into a public internet-egress NAT gateway.",
  note="Update the private subnet route tables and assess the gateway-hour cost against saved cross-AZ charges; this is not an unconditional claim that more gateways always cost less.")
a(143,"A","endpoint","Secrets Manager private access uses an interface VPC endpoint, not a gateway endpoint.",
  "A Secrets Manager interface endpoint provides private ENIs and supports endpoint-policy/security-group access controls.",
  "A Site-to-Site VPN is a hybrid network connection, not the native VPC-to-Secrets-Manager endpoint mechanism.",
  "Gateway endpoints are for supported S3/DynamoDB access, not Secrets Manager.",
  "A NAT path to a public service endpoint does not supply the requested private endpoint design.")
a(144,"C","costtags","Tag resources in their owning accounts, then analyse activated cost-allocation tags centrally.",
  "A member's own billing view does not provide the management account's full organisation-wide combined view.",
  "The management account does not automatically gain permission to tag every member-owned resource directly.",
  "Member accounts apply consistent tags; the authorised management billing view combines spend and account/tag breakdowns.",
  "CloudTrail activity logs are not the authoritative detailed billing source for NAT gateway charges.",
  note="Activate relevant tags in billing and use consolidated cost reporting. Member tagging may be performed through appropriately authorised cross-account automation.")
a(145,"B","iam","A Lambda execution role needs permission to create/write the required CloudWatch log resources.",
  "Kinesis-triggered Lambda invocations can publish CloudWatch Logs when their permissions and configuration allow it.",
  "Missing logs:CreateLogGroup, logs:CreateLogStream, or logs:PutLogEvents permissions can prevent expected log publication.",
  "CloudTrail records supported API activity; it is not the destination for ordinary function print/logger output.",
  "Active tracing controls distributed tracing, not the basic permission to write CloudWatch Logs.")
a(146,"AE","objectlock","Apply legal holds to the protected object versions and isolate temporary documents from their retention policy.",
  "A legal hold has no preset expiry and protects the selected versions while the hold remains active.",
  "A blanket default retention period would also protect temporary documents and is not the requested selective indefinite hold.",
  "Holding temporary documents would prevent the deletion behaviour that the requirement explicitly needs.",
  "A blanket DeleteObject denial also restricts temporary objects and is not an indefinite version-specific legal hold.",
  "A separate non-locked bucket is a straightforward offered way to keep temporary documents outside the formulation retention design.",
  note="Legal holds can be removed by authorised principals; they are not a promise of irreversible perpetual retention. Object Lock protects versions, and a separate bucket is one valid isolation choice rather than a universal requirement.")
a(147,"A","scp","Enable S3 Block Public Access and prevent member accounts from disabling the required settings.",
  "Account-level Block Public Access plus suitable SCP restrictions prevents member-account principals from weakening the required controls.",
  "Allowing accounts to disable the protection contradicts the central enforcement requirement.",
  "Legacy ACL handling is not the same as centrally enforcing Block Public Access across the accounts.",
  "Handcrafted bucket policies alone are harder to enforce consistently and do not provide the stated account-level protection setting.",
  options=["Enable Amazon S3 Block Public Access at the account level and use an AWS Organizations SCP to prevent accounts from disabling the required settings.","Enable account-level Block Public Access but allow member accounts to modify the settings when required.","Use S3 ACLs and configure SCPs to block public permissions.","Use S3 bucket policies to deny public access and enforce policy restrictions through SCPs."],
  note="Source-faithful transcription repair joins the first option's wrapped continuation. SCPs do not protect the management account; govern its settings separately.")
h(148,"peering","Both peering choices imply that on-premises traffic can traverse VPC B's Direct Connect attachment and then the B–A peering connection. VPC peering does not support that edge-to-edge transit. A complete design needs appropriate direct hybrid connectivity to VPC A or a supported gateway/TGW architecture, which is absent.")
a(149,"B","kms","Related multi-Region KMS keys can support local cryptographic operations on the same compatible ciphertext.",
  "Centralising all data can increase global latency and does not preserve the stated distributed architecture.",
  "Multi-Region replicas share compatible key material/IDs while local regional KMS endpoints handle supported operations.",
  "Disabling encryption violates the security requirement rather than improving a secure design.",
  "Ordinary single-Region KMS keys are regional and are not automatically available in every Region.",
  note="The application or integrated encryption design must support multi-Region keys. Each replica has its own policy and regional configuration; not every AWS service treats related keys as interchangeable.")
a(150,"D","polly","Polly turns existing text into natural-sounding speech.",
  "Rekognition analyses images/video rather than synthesising speech from quiz text.",
  "Textract extracts information from documents; the quiz text is already available.",
  "Comprehend analyses language meaning and entities but is not a text-to-speech engine.",
  "Polly is the managed speech-synthesis service for reading the existing question and option text aloud.")
a(151,"A","rds","Pool idle and active relational connections with RDS Proxy before simply increasing database size.",
  "RDS Proxy reuses backend connections and can reduce connection churn and the number of database sessions needed.",
  "A larger instance may mask connection pressure at higher cost without addressing idle connection reuse.",
  "Traditional Multi-AZ standby capacity improves availability rather than pooling application connections.",
  "Read replicas offload suitable reads but do not directly solve idle client connection churn on the primary.",
  note="Connection pooling does not optimise intrinsically slow SQL. Inspect query/index/transaction behaviour separately if slowness remains after connection pressure is addressed.")
a(152,"D","xray","Distributed tracing follows a request through instrumented services, including supported SQS integrations.",
  "CloudTrail records supported API activity but does not produce this end-to-end application trace by itself.",
  "Inspector scans supported software vulnerabilities rather than tracing message-processing paths.",
  "CloudWatch provides useful metrics/logs, but the specifically requested cross-component request tracing is X-Ray's role.",
  "With supported instrumentation and propagated trace context, X-Ray helps follow message-related work and identify failed/slow hops.",
  note="Tracing requires supported SDK/agent/OpenTelemetry instrumentation and context propagation; enabling a console service alone cannot reconstruct every uninstrumented message path.")
a(153,"B","cfnfull","Mappings provide a predefined lookup table for region-specific AMI IDs.",
  "Outputs expose values from a stack; they are not the region-to-AMI lookup definition.",
  "Define a mapping and use Fn::FindInMap with the appropriate Region/type keys to select an AMI.",
  "Parameters accept supplied values; they do not alone encode the predefined region lookup table.",
  "Conditions control supported conditional behaviour rather than defining the AMI lookup data.")
a(154,"A","video","Ingest video, extract suitable images, then use the Rekognition protective-equipment API for face-cover analysis.",
  "This combines the appropriate live-video ingestion with image-frame analysis using DetectProtectiveEquipment.",
  "Textract extracts document information, not protective equipment from people in CCTV frames.",
  "Comprehend analyses language rather than identifying face coverings in video images.",
  "A completed-video storage and generic-label flow does not specify the requested near-real-time frame/PPE analysis.",
  note="Frame extraction, invocation, confidence thresholds, and handling results still need implementation. Rekognition's protective-equipment API analyses images rather than directly accepting an arbitrary live-video stream.")
a(155,"A","sqs","Persist files in S3 and put their references in SQS to buffer bursty asynchronous processing.",
  "S3 preserves the uploaded payload, and SQS buffers durable processing work so workers can retry at their own rate.",
  "A relational file store and notification topic add cost/complexity and do not express an independent durable work backlog as directly.",
  "Metadata alone does not preserve the actual document if an upload later fails.",
  "EFS and MQ can support other architectures, but add unnecessary filesystem/broker concerns for this object-plus-work-queue requirement.",
  note="Use idempotent processing, suitable visibility/retention settings, and a DLQ. SQS stores a file reference, not arbitrary multi-megabyte documents.")
a(156,"A","acm","An email-validated ACM certificate may require renewal validation; inspect the pending-validation renewal status and complete it.",
  "Email validation can require the domain owner to respond to renewal approval messages before ACM can complete renewal.",
  "The supplied status does not establish that the certificate is already expired or inherently non-renewable.",
  "Pending validation requires investigation/action; assuming renewal will complete without validation can cause expiry.",
  "Support cannot simply bypass the required domain validation for a manual renewal.",
  note="The source's validity period is historical and certificate status versus renewal status is abbreviated. Inspect the actual expiration and renewal-validation state; DNS validation is another supported approach for managed renewal.")
a(157,"B","steps","Step Functions makes a sequence of serverless processing steps explicit, observable, and retryable.",
  "Batch schedules batch computing work rather than directly providing this application's visual multi-step orchestration.",
  "A state machine models order steps, branching, retries, and execution state without hand-built tracking between functions.",
  "SQS buffers messages but does not itself describe the state transitions of the whole workflow.",
  "Glue is for data integration/ETL, not the natural order-acceptance workflow coordinator.")
a(159,"B","sqs","An SQS resource policy can authorise cross-account sends without a separate assume-role hop.",
  "An identity policy in the receiving account cannot simply be attached to unrelated external account identities.",
  "A queue policy grants suitable external principals SendMessage access; sender identity permissions and encryption permissions must also be correct.",
  "Cross-account role assumption can work, but adds a role/session step that this direct resource-policy design does not need.",
  "Both designs can be valid, but they are not necessarily equally efficient; direct queue-policy access is the simpler offered path here.")
a(160,"D","steps","Use durable queued work and explicit workflow retries/compensation for multi-service asynchronous failures.",
  "Changing every API to synchronous does not create a supported atomic distributed transaction across arbitrary services.",
  "Unbounded custom retries can repeat side effects and do not provide a controlled compensation strategy.",
  "Manual support notifications do not implement the requested reliable automatic workflow handling.",
  "Step Functions can model retries and compensating actions while SQS buffers work durably between supported components.",
  note="Compensation is application-designed saga behaviour, not an automatic rollback of every external side effect. Make tasks idempotent and define failure limits/DLQs.")
a(161,"D","iam","Use workforce federation and IAM Identity Center for supported AWS account and application SSO.",
  "Separate IAM users and repeated application logins contradict the requested federated single sign-on experience.",
  "Social web identity providers do not preserve the stated corporate Active Directory workforce identity flow.",
  "SAML role federation provides AWS access, but alone does not express the broader managed application SSO configuration.",
  "Identity Center with a supported identity-source/federation integration centralises workforce access to AWS and configured applications.",
  note="Configure supported AD/IdP integration and application federation explicitly; existing arbitrary portals and SaaS applications do not gain SSO merely because Identity Center is enabled.")
a(162,"A","efs","Use a shared filesystem for concurrent ordinary file access from pods on different nodes.",
  "Encrypted EFS with the supported CSI driver provides shared NFS access independent of a single EKS worker node.",
  "General-purpose SSD EBS does not support the claimed Multi-Attach option.",
  "Supported io1/io2 Multi-Attach is AZ-scoped block access requiring coordinated software, not a general shared filesystem for arbitrary pods.",
  "An HDD EBS volume is an AZ-local block device rather than this multi-node shared file service.")
a(163,"D","secrets","Mount centrally managed secrets using supported EKS integrations and least-privilege pod identity permissions.",
  "Baking secrets into an image exposes them to image readers and makes rotation require replacing the image.",
  "ConfigMaps are configuration objects, not the appropriate secure central secret-management solution.",
  "Manual secret copying adds synchronisation and rotation overhead and can leave stale application copies.",
  "The provider/CSI integration retrieves permitted Secrets Manager values, and IRSA scopes access to the application's service account.",
  note="EKS Pod Identity is another supported choice for appropriate workloads. Use a supported node/driver configuration and configure rotation/refresh semantics; a mounted secret is not automatically consumed by the app.")
a(165,"B","fargate","ECS on Fargate runs independently scalable container services without managing an EC2 server fleet.",
  "EC2 Auto Scaling still requires managing the instance-based application fleet and does not directly provide container-service orchestration.",
  "ECS services on Fargate meet the existing-container and no-server-management requirements with supported AWS integrations.",
  "Rewriting each existing containerised service as a Lambda function is unnecessary and introduces invocation/runtime constraints.",
  "Self-managed EC2 worker nodes retain the server-management responsibility that the requirement wants to remove.")
a(167,"C","cloudwatch","ALB publishes native CloudWatch metrics; create alarms on the appropriate request, latency, and error metrics.",
  "A guest agent collects instance metrics/logs, not the service's native ALB metrics.",
  "Access logs help detailed investigation, but querying them is not the lowest-effort native metric-alarm path.",
  "Use ALB's published CloudWatch metrics and suitable alarms without installing an agent on the load balancer.",
  "Tracing provides request-level evidence but is not the simplest way to alarm on native aggregate ALB metrics.")
a(168,"BC","inspector","Compute Optimizer recommends supported resource sizing; Security Hub can report supported public-S3 security-control findings.",
  "GuardDuty targets suspicious activity rather than producing the requested EC2 rightsizing recommendations.",
  "Compute Optimizer analyses supported utilisation evidence and recommends more suitable EC2 configurations.",
  "With the relevant standards, recording, and controls configured, Security Hub can surface public-S3 posture findings.",
  "Inspector targets supported workload vulnerabilities and exposure rather than EC2 cost rightsizing.",
  note="Use the relevant Security Hub/Config controls and recording prerequisites; a findings dashboard alone neither fixes every bucket nor prevents all future public access.")
a(169,"B","athena","Athena queries suitable S3 files with SQL without first copying them into a database.",
  "Building ETL and loading a warehouse is more work than the direct SQL-over-S3 requirement needs.",
  "Athena supports SQL queries over appropriately described CSV data in S3 without a local download.",
  "EMR/Hive can query data but introduces processing-environment overhead for this straightforward task.",
  "Loading the files into RDS creates an additional database and ingestion lifecycle.",
  note="Source-faithful OCR correction: 'SS' means S3. Use a suitable table/schema; columnar formats and partitioning may improve larger-scale performance.")
a(170,"A","cfnoutputs","Export a value from Outputs and use Fn::ImportValue for supported cross-stack references.",
  "An exported output can expose the security-group ID to another stack using Fn::ImportValue.",
  "Mappings provide static lookup data rather than a live value exported by a different stack.",
  "Parameters accept input; they do not alone establish an automatic cross-stack export/import reference.",
  "Conditions choose conditional template behaviour, not the cross-stack value-sharing mechanism.")
a(171,"C","sqs","A durable queue absorbs asynchronous write bursts while workers drain at a sustainable database rate.",
  "Vertical scaling conflicts with the stated preference and does not add the desired burst buffer.",
  "Changing the entire database/data model is disproportionate when the writes can be queued and processed later.",
  "SQS decouples accepted work from write execution so workers can rate-limit and retry database operations.",
  "MQ is appropriate for supported broker-protocol compatibility needs, which are not stated here; SQS has less broker management.",
  note="A queue does not increase the database's sustained write capacity. Provision enough drain capacity and define acceptable backlog delay and retention.")
a(172,"C","s3","Glacier Instant Retrieval fits rarely accessed long-lived objects that still need millisecond retrieval.",
  "Standard provides online access but its storage price is not the best fit for this rare-access archive.",
  "Standard-IA supports immediate access but Glacier Instant Retrieval is the archival candidate for this described long-lived rare-access pattern.",
  "Glacier Instant Retrieval combines archival storage pricing with millisecond object retrieval, subject to retrieval/minimum-duration charges.",
  "One Zone-IA reduces AZ resilience, which is inappropriate for these irreplaceable records unless additional copies are designed.",
  note="Compare request/retrieval charges and object sizes in a real cost estimate. Storage class alone does not enforce a five-year retention policy.")
a(173,"A","mgn","Outposts brings supported AWS infrastructure to the customer's premises.",
  "Outposts provides supported AWS-managed infrastructure on-premises, fitting the explicitly requested hybrid placement.",
  "Snowball is a specialised offline transfer/edge device, not the general supported AWS rack infrastructure described.",
  "Storage Gateway provides supported hybrid storage interfaces, not on-premises application compute infrastructure.",
  note="The complete source offers three choices. This clarified question asks for AWS infrastructure on-premises, unlike older ambiguous wording that implied moving an arbitrary on-premises database into an AWS Region.")
a(174,"D","glue","Lake Formation coordinates data-lake setup and fine-grained access; Glue jobs perform the actual cleansing transformations.",
  "Spectrum queries external data from Redshift; it is not the central data-lake governance and ingestion service described.",
  "A warehouse can support analytics but is not the offered fine-grained managed data-lake governance service.",
  "The Glue Data Catalog describes datasets; a catalogue alone does not enforce the entire requested ingestion and permissions workflow.",
  "Lake Formation provides data-lake governance and supported fine-grained access controls, integrating with Glue for ingestion and cleansing.",
  note="Do not infer that a Lake Formation permission automatically deduplicates or removes anomalies. Configure the Glue transformations and the supported engine/table-level fine-grained permissions.")
a(176,"D","efs","EFS One Zone-IA targets cold, recreatable file data when loss of the single AZ is acceptable.",
  "Regional Standard retains a higher-cost hot-data and multi-AZ profile than the stated recreatable cold copy needs.",
  "One Zone addresses the AZ cost tradeoff but its hot tier does not exploit the stated infrequent access as directly.",
  "Regional IA supports cold data but pays for a broader resilience scope than this recreatable single-AZ copy requires.",
  "One Zone-IA combines cold-file lifecycle pricing with the explicitly accepted single-AZ failure tradeoff.",
  note="One Zone-IA is reached through the supported One Zone filesystem lifecycle policy. Include retrieval/minimum billing considerations and verify throughput settings separately.")
h(177,"redshift","The source recommends AQUA as a separately selectable acceleration feature and omits the current Redshift configuration/workload context needed to diagnose CPU/network bottlenecks. Old AQUA feature-selection material does not establish a supported present-day tuning action; Spectrum and caching also do not automatically resolve the stated bottleneck.")
a(178,"B","eks","EKS Anywhere is the supported customer-managed Kubernetes lifecycle product for suitable on-premises environments.",
  "ECS Anywhere extends ECS orchestration; it is not the requested Kubernetes platform.",
  "EKS Anywhere provides supported on-premises Kubernetes deployment/lifecycle tooling based on the EKS distribution.",
  "EKS Distro is the Kubernetes distribution and components, not the complete EKS Anywhere lifecycle-management product.",
  "Ordinary regional EKS managed control planes are not equivalent to deploying a customer-managed on-premises EKS Anywhere cluster.",
  note="The source's AWS-control-plane language is loose: EKS Anywhere is customer-managed and does not mean AWS remotely operates every on-premises control plane. Check supported infrastructure and integration capabilities.")
a(179,"A","ebs","Recycle Bin retention rules can recover supported accidentally deleted snapshots and EBS-backed AMIs.",
  "Configured Recycle Bin rules retain eligible deleted AMIs for recovery during the retention period.",
  "StackSets deploy templates across targets; they do not act as an undelete service for arbitrary AMIs.",
  "Beanstalk deploys application environments and does not provide this general AMI recovery control.",
  "Reconstructing from snapshots can work but is more manual than using configured AMI recovery retention rules.",
  note="Create appropriate retention rules before deletion and inspect the associated snapshot handling. Recycle Bin cannot retroactively recover an AMI that was never retained.")
a(181,"A","ebs","Use tested adequate gp3 performance for the database and throughput-oriented st1 for suitable sequential logs.",
  "The prompt establishes gp3 meets the database's tested requirements; st1 fits large sequential HDD-tolerant log processing.",
  "gp2 performance depends on volume size, and the option does not establish that the database targets are met cost-effectively.",
  "io2 is unnecessary when the tested gp3 configuration already meets the latency targets; gp3 adds SSD cost to HDD-tolerant sequential logs.",
  "io1 can meet some database targets but buys a higher-priced volume class without an unmet gp3 performance requirement.",
  note="Source-faithful OCR repairs: st1/sc1/io1/io2 names were confused with letters. Do not reuse the outdated blanket rule that more than 16,000 IOPS always requires io1/io2.")
a(183,"C","kms","Symmetric encryption key type and customer-managed ownership are different dimensions.",
  "Asymmetric keys do not match the requested 256-bit symmetric encryption/decryption key type for these integrated-service patterns.",
  "CloudHSM is a dedicated cryptographic hardware service, not a KMS key type.",
  "A supported symmetric KMS encryption key uses protected 256-bit symmetric material for integrated encryption/envelope-encryption operations.",
  "Customer managed describes ownership/control; such a key could be symmetric or asymmetric, so it does not answer the type question.",
  note="Do not assume one arbitrary key can be substituted transparently into every S3/Lambda/DynamoDB integration. Configure each service's supported encryption and permissions separately.")
a(184,"C","lex","Lex provides managed conversational interfaces with supported intent, context, and Lambda integrations.",
  "Polly produces speech from text; it does not manage the complete conversational intent flow.",
  "Comprehend analyses text but does not by itself run the chatbot's multi-turn conversation.",
  "Lex models conversational intents and turns and supports Lambda hooks for backend fulfilment.",
  "Transcribe turns audio into text rather than supplying the complete contextual chatbot interaction.")
a(186,"C","kmspolicy","Use a supported KMS custom key store when RDS encryption must rely on a customer-controlled CloudHSM-backed KMS key.",
  "A direct CloudHSM-backed Oracle TDE integration is not established for this standard RDS configuration.",
  "Naming MariaDB and CloudHSM does not specify a supported RDS encryption-at-rest key integration.",
  "A supported customer-managed KMS key in a CloudHSM custom key store can be selected for compatible RDS encryption without application cryptography changes.",
  "A standard KMS key does not meet the explicit customer-controlled single-tenant CloudHSM key-store requirement.",
  prompt="A bank deploys a supported Amazon RDS database. Its vendor manages database administration and backups through supported RDS interfaces. Encryption at rest must use a KMS key whose material is protected by a customer-controlled, single-tenant CloudHSM cluster, without application-level encryption changes. Which offered configuration fits?",
  note="Editorial clarification removes the implication that a third-party administrator gets arbitrary RDS operating-system/database-file access. Verify custom-key-store and engine support; keep the CloudHSM cluster available.")
a(187,"B","waf","Combine supported Shield Advanced protections with WAF application-layer rules and visibility.",
  "Threat detection and investigation tools do not provide this inline DDoS mitigation and custom HTTP filtering combination.",
  "Shield Advanced supplies supported enhanced DDoS capabilities, and WAF provides application-specific request controls.",
  "Shield Standard gives baseline DDoS protections but omits the advanced capabilities requested by the maximum-protection scenario.",
  "Inspector vulnerability scanning and Detective investigation are not a DDoS mitigation layer.",
  note="Associate protections with supported resources. WAF requires a supported HTTP-facing resource such as an ALB, not every ELB type.")
a(189,"D","endpoint","aws:SourceVpce restricts a request context to a particular VPC endpoint.",
  "An internet proxy violates the requested private endpoint path and introduces an unnecessary instance.",
  "NAT and NACL rules do not enforce key-use permissions originating through one specific endpoint.",
  "aws:SourceVpc identifies a VPC and is broader than a restriction to one endpoint.",
  "A KMS interface endpoint plus appropriate aws:SourceVpce policy conditions scopes supported requests to the chosen endpoint.",
  note="Endpoint conditions supplement, not replace, identity/key authorisation. Consider AWS service calls that may not carry the same endpoint context before writing blanket denies.")
h(190,"discovery","The intended historical answer is Application Discovery inventory/dependency collection, but AWS Application Discovery Service is no longer available to new customers. This new assessment establishes no customer eligibility, and its captured inventory option is also incomplete. Current migration-assessment alternatives must be evaluated rather than scoring an unconditional historical recommendation.")
h(194,"neptune","The question conflates generating graph-based recommendations with low-latency serving of precomputed recommendation/user-interaction values. Redis and Neptune address different data models, but the source states neither a relationship-traversal requirement nor a precomputed-result serving model, preventing a uniquely supported answer.")
h(195,"kinesis","No option is technically complete: MSK does not offer general multi-cloud deployment or SSH access; Lambda needs a supported event source mapping; provisioned MSK storage autoscaling is not automatic arbitrary broker-count scaling. Serverless MSK differs, but the offered broker-and-storage claim does not specify that architecture.")
a(196,"C","search","OpenSearch provides supported full-text, synonym, and typo-tolerant search capabilities.",
  "QuickSight visualises analytics; it is not the product full-text search index.",
  "Step Functions coordinates workflows, not text indexing and search ranking.",
  "OpenSearch indexes product text and supports suitable analyzers, synonym configuration, and fuzzy queries.",
  note="The complete captured source offers three choices. Configure analyzers/query logic appropriately; a newly created domain does not automatically implement every desired relevance rule.")
h(197,"comprehend","Several listed service pairs could participate in a streaming analytics system, but none specifies the complete feedback ingestion, sentiment extraction, and visualisation pipeline. Kinesis/Redshift and MSK/QuickSight can both be components; the omitted NLP and integration requirements prevent a single fully supported choice.")
a(198,"A","dataexchange","Data Exchange acquires and manages supported third-party data products and subscriptions.",
  "Data Exchange supplies supported third-party data subscriptions, licensing workflows, and delivery/access mechanisms.",
  "Kinesis ingests/processes streams but is not a marketplace subscription service for external datasets.",
  "Data Pipeline was a workflow service, not the external-data product subscription capability described.",
  "EMR processes large datasets; it does not manage the acquisition/licensing of third-party data products.")
h(199,"kinesis","Both Kinesis Data Streams and Amazon MSK can build highly scalable real-time streaming platforms with downstream consumers. The source does not require Kafka compatibility, a particular consumer ecosystem, replay model, or an operational objective that would distinguish the two; selecting one solely from the word streaming would be a keyword shortcut.")
a(200,"D","comprehend","Comprehend extracts supported language insights such as sentiment and entities from text.",
  "Lex runs conversational interfaces rather than batch analysis of existing support tickets.",
  "Textract extracts document text/structure; the task here concerns meaning in ticket text.",
  "SageMaker can host custom models but requires more model work than the managed NLP capabilities requested.",
  "Comprehend supplies managed sentiment/entity and supported topic-analysis operations for suitable text inputs.",
  note="Potential solution recommendations still require application logic or another retrieval/generation system; sentiment/entity analysis does not automatically resolve customer tickets.")
a(201,"D","lex","Lex is the managed conversational interface for natural-language customer enquiries.",
  "Rekognition analyses visual content rather than running text conversations.",
  "Comprehend extracts text insights but is not the conversational interaction manager.",
  "Polly supplies text-to-speech output, not the chatbot's intent/dialogue logic.",
  "Lex supports natural-language intents, text conversations, and backend fulfilment integrations.")
a(202,"D","textract","Textract extracts supported text, tables, forms, and queried fields from scanned documents.",
  "Polly synthesises speech and does not extract fields from scanned invoices.",
  "Generic image recognition is not the dedicated document-text/form extraction capability requested.",
  "A custom SageMaker pipeline requires more model/application work than the supported managed extraction service.",
  "Textract performs OCR and supported structured document analysis so downstream code can use extracted fields.",
  note="Extracting text or a field is not automatically legal interpretation of a contractual clause. Configure supported queries/adapters or downstream language analysis when required.")
a(203,"D","kendra","Kendra supplies managed enterprise search over supported document sources and connectors.",
  "OpenSearch can underpin custom search, but the specified managed enterprise connectors and natural-language retrieval fit Kendra more directly.",
  "Comprehend analyses language rather than providing a full enterprise document search index and connector layer.",
  "Lex runs conversations and can call search, but is not itself this enterprise document-indexing service.",
  "Kendra provides supported document-source connectors and managed enterprise search capabilities.",
  prompt="An enterprise wants a managed enterprise search service with supported document-source connectors and natural-language retrieval across PDFs, Word documents, emails, FAQs, and internal knowledge repositories. Which listed service most directly supplies that enterprise indexing and search capability?",
  note="Editorial clarification makes the managed enterprise-search/connector requirement explicit, distinguishing it from building a custom search application on OpenSearch.")
a(204,"D","rds","Traditional RDS Multi-AZ DB instance failover changes the endpoint's DNS target to the promoted standby.",
  "Do not model the failover as moving the old primary's fixed IP address to a different machine.",
  "A Multi-AZ failover can promote the existing standby rather than waiting only for the original instance to recover.",
  "A standby is already available; creating an entirely new replacement first is not the normal failover description.",
  "RDS updates the endpoint's DNS target to the promoted standby; clients reconnect using the same database endpoint.",
  note="Respect DNS TTL and connection retry behaviour. The question specifies a traditional DB instance deployment, not a three-instance Multi-AZ DB cluster.")
a(205,"D","auroraha","Aurora's shared multi-AZ storage and low-lag replicas are a strong architectural fit for a growing compatible relational workload.",
  "RDS MySQL supports relational workloads but ordinary asynchronous replicas do not supply Aurora's shared-storage replication architecture.",
  "DynamoDB requires a different NoSQL access model and is not a drop-in MySQL-compatible database migration.",
  "Redshift targets warehouse analytics rather than the application's MySQL transactional database.",
  "Aurora MySQL compatibility, scalable storage, and low-lag replicas make it the strongest listed architecture to evaluate.",
  note="A sub-100 ms replica-lag requirement is a target to benchmark, not an unconditional service guarantee. Current RDS storage limits also mean 15–30 TB alone no longer uniquely selects Aurora.")
a(206,"D","vpn","Use supported private hybrid networking and native MySQL replication for an external on-premises replica.",
  "TLS over the internet can secure replication traffic, but a suitable private hybrid path is the more direct offered secure architecture.",
  "An intermediate EC2 replica adds a replication hop and operational components without a stated need.",
  "Periodic backup/restore does not maintain a continuously replicating read copy.",
  "An appropriate VPN or encrypted Direct Connect design can carry supported native MySQL replication to the external server.",
  note="Direct Connect is not encrypted by default; use supported TLS/IPsec/MACsec where required. Configure binlog retention, replication users, initial seeding, and supported engine settings.")
a(207,"D","cfnfull","Snapshot a supported database on stack deletion and retain the S3 bucket itself.",
  "Replication creates another data lifecycle and does not itself retain the original stack's S3 bucket resource.",
  "Retaining both keeps the live database and its costs rather than the requested database snapshot disposition.",
  "S3 buckets do not support CloudFormation's Snapshot deletion policy.",
  "Snapshot on RDS preserves a supported backup; Retain on S3 leaves the bucket and its objects after stack deletion.")
h(208,"dynamo","Provisioned DynamoDB auto scaling reacts with delay and does not guarantee that an unpredictable instantaneous jump from 1,000 to 3,000 WCU is served without throttling. The question demands consistent burst capacity but omits on-demand mode or provisioned headroom/burst timing, so the intended auto-scaling answer is not a complete guarantee.")
a(209,"D","aurora","Aurora read-replica auto scaling addresses variable read demand while a suitable multi-AZ cluster supports availability.",
  "DynamoDB is not a single primary relational node and requires a different data model from PostgreSQL.",
  "A Single-AZ primary with ordinary read replicas does not describe the strongest managed HA and automatic replica scaling choice offered.",
  "RDS does not let the customer choose Spot instances for its managed database servers.",
  "Aurora PostgreSQL with suitable replicas/failover configuration and replica auto scaling matches the stated read-heavy demand.",
  note="PostgreSQL 9.2 is obsolete; assess version upgrades, extension compatibility, and migration steps. Aurora replica scaling is not instantaneous or automatic writer-compute scaling.")
a(210,"D","secrets","Secrets Manager stores supported database secrets and manages their rotation lifecycle.",
  "Parameter policies provide supported expiration/notification behaviour, not native automatic RDS password rotation.",
  "A custom S3/Lambda secret store duplicates lifecycle work supplied by Secrets Manager.",
  "An EC2 IAM role authorises AWS API calls but does not by itself implement arbitrary database-password rotation; IAM DB auth is a separate supported design.",
  "A supported Secrets Manager rotation integration manages the password lifecycle while the application retrieves the current secret using its role.")
h(211,"dr","The question does not specify whether recovery is from corruption/deletion or a regional outage. Global Tables can replicate bad writes/deletes, while PITR/backup restore duration depends on table size and is not guaranteed within one hour. The source omits failure scope and tested restore evidence, so the strict objectives cannot select a uniquely complete design.")
a(212,"D","dms","DMS CDC maintains supported source/target changes during migration; heterogeneous schema conversion is a separate prerequisite.",
  "Snapshots are point-in-time copies, not continuous cross-engine change replication.",
  "DataSync copies files/objects and does not translate native MySQL changes into PostgreSQL database operations.",
  "Aurora Global Database does not convert and replicate an arbitrary MySQL source into a PostgreSQL target.",
  "A supported DMS full-load/CDC migration keeps eligible data changes flowing during the transition.",
  note="Convert and validate the heterogeneous schema/code with SCT or suitable DMS schema-conversion tooling; configure compatible source logging and plan a controlled cutover.")
a(213,"D","serverless","Aurora Serverless v2 adjusts supported compute capacity within configured bounds for variable demand.",
  "Fixed provisioned capacity can pay for unused quiet-period compute and requires capacity planning.",
  "Hand-built scheduled resizing does not naturally match unpredictable evening demand and adds operational work.",
  "Multi-AZ improves availability rather than making database compute automatically scale with demand.",
  "Aurora Serverless v2 scales supported capacity with workload demand subject to configured limits and engine capabilities.",
  note="Aurora stores tables inside a cluster/database. Zero-capacity auto-pause requires supported engine versions/configuration; do not assume every Serverless v2 cluster always scales to zero.")
a(214,"BD","sqs","Long polling reduces empty receives; batching reduces API calls per processed message.",
  "Sleeping a full minute between receives delays available messages and violates the processing-latency goal.",
  "Long polling waits for available messages rather than returning repeated empty short-poll results.",
  "Short polling can keep generating empty responses and does not address the API-call cost problem.",
  "Supported receive/delete batches process multiple messages per API request, reducing request overhead.",
  "FIFO ordering/deduplication is not a mechanism to eliminate empty polling responses.")
a(215,"D","sqs","Visibility timeout must accommodate processing, and consumers should still make writes idempotent.",
  "A newly created queue does not correct the processing-duration versus visibility-timeout mismatch.",
  "Long polling affects how receives wait for messages, not how long a received message is hidden.",
  "Restricting to one consumer sacrifices parallelism and does not provide a general robust duplicate-handling design.",
  "Increasing or extending visibility prevents ordinary reappearance while the current worker is still processing.",
  note="SQS Standard can still redeliver a message. Use idempotent/conditional DynamoDB writes to avoid repeated business effects even after visibility is tuned.")
a(216,"D","sns","A separate SQS backlog between SNS and Lambda decouples notification delivery from worker availability.",
  "More memory/runtime does not preserve an event that could not be delivered through the source path.",
  "Orchestration alone does not insert the requested durable per-consumer backlog into this notification delivery path.",
  "Monitoring identifies failures but is not itself durable ingestion and automatic retry.",
  "SNS-to-SQS fanout with a Lambda event source mapping provides a durable work queue and controlled retries.",
  note="SNS and asynchronous Lambda already have retry capabilities; this adds queue retention/visibility/DLQ control rather than claiming SNS never retries. Configure permissions, idempotency, and failure handling.")
a(217,"D","steps","Use a state machine to coordinate and observe the steps of a serverless workflow.",
  "EC2 and custom scripts retain server and workflow-state management that the requirement wants to minimise.",
  "Queue/function/topic components can decouple events, but do not by themselves define the stated multi-step orchestration.",
  "Beanstalk and RDS describe another application hosting model, not this primarily serverless workflow coordinator.",
  "Step Functions with Lambda models the workflow steps and failures, with suitable S3 object storage for its data.")
a(218,"D","sqs","SQS-triggered Lambda can process independent durable jobs, with large job payloads retained in S3.",
  "A direct load-balanced application plus RDS does not express the durable decoupled work queue as directly.",
  "ECS/Fargate can process jobs, but this option omits a triggering/queueing design for dynamically consuming outstanding work.",
  "ElastiCache is not the suitable sole durable store for important batch job payloads.",
  "SQS supplies the durable job backlog, S3 stores payloads, and a supported Lambda mapping scales processing within configured limits.",
  note="Jobs must fit Lambda's runtime/resource limits. Configure concurrency, idempotency, retention, and failure handling; use container workers for unsuitable long-running jobs.")
h(219,"sqs","The source requires strict order 'for all consumers' without defining one queue, per-key ordering, independent readers, or global ordering. SQS FIFO orders within message groups, while Kinesis orders within its stream partition model; neither offered generic configuration guarantees universal total order for unspecified consumers. The consumer/ordering scope must be stated.")
a(220,"C","sqs","Idempotent processing prevents duplicate business effects even if a message causes another invocation.",
  "S3 event notifications cannot directly target an SQS FIFO queue in this design, and FIFO is not a blanket exactly-once side-effect guarantee.",
  "An arbitrary delay does not determine whether an image has already been processed and emailed.",
  "Store a processing/deduplication key and make the effect idempotent so a repeated event does not send another email.",
  "Zero visibility lets other workers immediately see the same message and can increase concurrent duplicate work.",
  prompt="S3 events are delivered to an SQS Standard queue consumed by Lambda. At-least-once delivery can repeat an image event, causing duplicate emails. What is the best offered way to prevent duplicate email side effects with minimal architectural change?",
  note="Editorial correction: idempotency prevents duplicate effects, not duplicate Lambda invocations themselves. Use an appropriate atomic deduplication/side-effect protocol.")
a(221,"B","s3endpoint","A VPC-connected Lambda needs an actual network path to S3; subnet placement alone does not provide one.",
  "Low memory can affect processing performance, but a network timeout reaching S3 specifically points first to connectivity.",
  "A suitable S3 gateway endpoint or NAT path and associated routing can provide the otherwise missing service access.",
  "A missing bucket-name environment variable would cause an application/configuration error, not establish this network route.",
  "Different Regions can affect the design, but the stated symptom and private-subnet setup most directly indicate a missing path.",
  note="Check endpoint/identity/bucket permissions and security groups/NACLs too. Stream large files rather than assuming they must fit in memory or /tmp.")
a(222,"CE","lambda","Customers control function code/dependencies and IAM permissions; AWS manages the underlying Lambda servers.",
  "AWS manages the underlying managed execution infrastructure and operating-system patching for supported managed runtimes.",
  "AWS monitors service infrastructure; customers monitor their function/application behaviour, rather than managing the underlying execution host's health.",
  "The customer remains responsible for application logic and security of supplied libraries/dependencies.",
  "Customers package supported dependencies or container images; they do not install them by logging into Lambda's underlying hosts.",
  "The customer supplies an execution role with the permissions required by the function's AWS calls.",
  note="Customer-managed Lambda container images and runtime components have additional update responsibilities. This question distinguishes the application from AWS-managed host infrastructure.")
a(223,"D","lambda","Lambda /tmp is limited to 10 GB; downloading a 12 GB object in full to that disk exceeds the limit.",
  "A bounded log-processing function can react to supported CloudWatch log events and publish SNS notifications.",
  "EventBridge can schedule supported Lambda work such as a bounded resource-usage report.",
  "API Gateway and Lambda can form a scalable backend with suitable database connections and limits.",
  "The offered full download includes objects larger than Lambda's maximum ephemeral storage and cannot always fit as described.",
  note="Streaming or chunked analysis can change feasibility. This exclusion concerns the explicit full-file-to-/tmp design, not every possible analysis of a large S3 object.")
a(224,"ABD","lambda","Lambda qualifiers follow the function name with a colon, not a slash.",
  "The :$LATEST suffix represents the unpublished-version qualifier in this schematic Lambda function ARN.",
  "The unqualified function ARN identifies the function without selecting a published version or alias.",
  "A slash before $LATEST is not the Lambda qualifier syntax.",
  "A :PROD suffix can identify an existing alias named PROD in the schematic ARN.",
  options=["arn:aws:lambda:aws-region:acct-id:function:helloworld:$LATEST","arn:aws:lambda:aws-region:acct-id:function:helloworld","arn:aws:lambda:aws-region:acct-id:function:helloworld/$LATEST","arn:aws:lambda:aws-region:acct-id:function:helloworld:PROD"],
  note="Source-faithful visual transcription repairs spaces and the OCR '$LATEST' glyph. aws-region/acct-id are placeholders; use real values in an actual ARN. Alias existence and supported operation semantics are separate checks.")
a(225,"B","privateapi","A supported API Gateway VPC Link integration can reach private on-premises targets through an NLB and hybrid connectivity.",
  "Supported private integrations can reach a suitable load balancer whose targets are reachable over hybrid networking.",
  "VPC Link to an appropriate NLB and supported on-premises IP targets over Direct Connect provides the offered private integration pattern.",
  "Using the public HTTPS endpoints does not meet the requested private backend path.",
  "Direct Connect is network transport, not a selectable API Gateway AWS-service backend integration that invokes arbitrary REST APIs.",
  note="Verify the API type, VPC Link generation, target-IP ranges, routing, TLS, and security groups. Other supported modern private-integration patterns may also be suitable.")
a(226,"AC","apigw","Throttle incoming API work and cache suitable repeatable responses to reduce backend pressure.",
  "Steady-state and burst throttling bound the volume passed toward the backend.",
  "A time-bound customer access policy is not the requested general performance and backend-load control.",
  "Caching suitable REST API responses avoids recomputing repeated requests at the backend.",
  "A load balancer distributes traffic but does not by itself impose API limits or avoid repeated backend computation.",
  "Restricting access to unauthenticated users is neither a load-management strategy nor appropriate customer authentication.",
  note="Cache only responses with correct cache keys/authorisation separation and freshness. Throttling is a best-effort control, not a guarantee that every downstream limit is impossible to exceed.")
h(227,"apigw","The source asks for exactly two non-access-control mechanisms, but server-side certificates, VPC route tables, and usage plans are not substitutes for API authentication/authorisation. Usage plans/API keys control consumption and should not be treated as a strong direct access-control mechanism, so the wording leaves more than two defensible choices.")
a(228,"C","waf","AWS supplies baseline managed DDoS protections; application and backend security configuration remains shared responsibility.",
  "CORS is not automatically a complete secure configuration, and it is not a general DDoS protection mechanism.",
  "A resource policy must be configured for the intended access needs; it is not the named default infrastructure protection.",
  "AWS's baseline managed DDoS protection is the relevant default service-side protection among these choices.",
  "AWS has service infrastructure protection responsibilities, so claiming it provides no default protection is false.",
  note="This does not mean AWS automatically secures all backend business logic, sets every suitable throttle, or provides every Shield Advanced/WAF feature at no cost.")
a(229,"C","apigw","API Gateway exposes supported cache sizing, encryption, and flush controls, not an import-cache feature.",
  "REST API stage caching offers supported cache-capacity choices.",
  "Cache encryption is a supported configuration for applicable cached methods/stages.",
  "There is no general console feature to import an arbitrary prebuilt API response cache.",
  "Flushing the cache is a supported cache-management action.")
a(232,"AB","s3endpoint","An endpoint policy restricts access but does not grant missing identity permissions to a new bucket.",
  "A policy allowing only an old bucket list can exclude the newly created bucket.",
  "The instance's credentials also need appropriate S3 identity/resource authorisation for the new bucket.",
  "Implicit deny can be overcome by an applicable allow; an explicit deny is what overrides an applicable allow.",
  "Gateway endpoint routes target a service prefix list, not a separate hostname route for each bucket.")
a(233,"B","vpn","A Direct Connect gateway supports suitable private connectivity to VPCs across multiple Regions.",
  "A public VIF reaches public AWS services, not a VPC's private virtual gateway in the claimed way.",
  "An appropriate Direct Connect gateway association design supports multi-Region VPC connectivity from the dedicated connection.",
  "Redundant private VIFs address resilience but do not alone state the required multi-Region gateway association design.",
  "A VPN over DX supplies encryption for a suitable path but does not by itself express multi-Region VPC connectivity.",
  note="Use supported gateway/VIF associations and plan connection redundancy separately. One DX gateway does not make one physical circuit highly available.")
a(234,"C","vpn","Use a private corporate network path and tightly scoped administration to private application resources.",
  "Public SSH access does not enforce access only from the organisation's internal network.",
  "A public bastion is still an internet-facing administration path unless further restrictions are specified.",
  "A corporate VPN with appropriately private bastion/application/database placement supplies the offered internal-network access architecture.",
  "A public Redshift placement unnecessarily exposes a component and does not match the private architecture objective.",
  note="Use least-privilege security groups and route controls. Systems Manager may remove the need for a bastion in a suitable design, but that option is not offered.")
a(235,"A","vpc","Restrict the target servers' inbound RDP rule to the bastion's security group.",
  "The target security group enforces that only traffic from the authorised bastion can reach the RDP listener.",
  "Restricting entry to the bastion is useful but does not remove other direct RDP paths to production servers.",
  "Blocking ports 22/443 does not establish the required allow-only RDP path on port 3389.",
  "A bastion NACL allowing 3389 does not restrict the production servers' RDP sources to the bastion.")
a(236,"AC","s3endpoint","Gateway-endpoint connectivity still depends on security-group egress and stateless NACL return-path rules.",
  "An outbound security-group restriction can prevent the instance's HTTPS traffic from reaching S3.",
  "S3 gateway endpoint traffic does not require a default route to an internet gateway.",
  "A stateless NACL must permit the return traffic on the required ephemeral ports and address ranges.",
  "A NAT gateway is unnecessary for the stated same-Region S3 gateway endpoint path.",
  "A missing IAM permission ordinarily causes an access denial, not the network timeout used to distinguish these answers.")
a(237,"B","peering","VPC peering cannot provide edge-to-edge transit through another VPC's NAT gateway.",
  "Adding routes cannot make the unsupported peering-to-NAT edge-transit path valid.",
  "A peer cannot use another VPC's NAT gateway through the peering connection as its internet-egress transit.",
  "Direct A–C peering does not supply the missing internet-egress transit capability.",
  "The source already places the working gateway in B's public subnet; its placement is not the differentiator.",
  note="Centralised egress can use a suitable Transit Gateway and inspection/routing design. Peering's non-transitive limits remain even when the route tables are edited.")
a(238,"B","vpc","Add a non-overlapping secondary VPC CIDR, then create subnets for the new capacity.",
  "A new VPC plus peering can create capacity, but adds another network when the existing VPC can be extended appropriately.",
  "A supported secondary CIDR extends the VPC's available addressing so new non-overlapping subnets can be created.",
  "Existing subnet CIDR blocks cannot simply be resized in place to reclaim addresses this way.",
  "Permissions and NACLs do not create additional IP address capacity in exhausted subnets.",
  note="The screenshot's OCR 'B subnets' means eight /27 blocks within /24; AWS also reserves addresses per subnet. Associate a valid non-overlapping secondary range and update routing/security as needed.")
a(239,"C","peering","Each subnet route table needs the remote permitted subnet range through the peering connection.",
  "A route to the full remote /16 is broader than the stated subnet-only routing scope.",
  "A full-VPC /16 route similarly exceeds the requested limited remote-subnet range.",
  "These reciprocal routes target the other VPC's specific allowed subnet through the peer.",
  "These destinations refer to each route table's own local subnet instead of the remote destination.",
  note="Narrow routing alone is not a complete security boundary. Apply matching security-group/NACL controls and assess other existing routes.")
a(240,"BD","ebs","EBS data can survive stop/start; instance-store lifecycle is tied to the instance/host.",
  "Instance-store data is not retained through stop/termination or underlying host failure.",
  "Persistent EBS volumes can retain data while a supported EBS-backed instance is stopped and restarted.",
  "Instance-store data can survive a reboot, but not the stated stop/start lifecycle.",
  "Instance store is determined at launch/instance-type selection and cannot later be attached as a detachable EBS-style volume.",
  "Not every EC2 instance type provides instance-store disks, even when it supports EBS.",
  note="On supported Nitro NVMe instances local devices are automatically enumerated; old explicit instance-store block-device mapping rules differ. EBS deletion on termination is separately controlled.")
a(241,"D","ebs","EBS encryption covers supported at-rest data, volume-to-instance traffic, and snapshots.",
  "This is true: the encrypted volume's stored data is protected at rest.",
  "This is true for the EBS encryption path: data moving between the volume and the instance is encrypted.",
  "This is true: snapshots created from an encrypted volume are encrypted.",
  "This is the false statement: current-generation EC2 instance types support EBS encryption.",
  note="The question asks for the NOT-true statement. EBS encryption does not automatically encrypt arbitrary application traffic to unrelated services.")
a(242,"D","ebs","You can request an encrypted new volume from an unencrypted snapshot; you cannot flip an existing unencrypted volume in place.",
  "Creating a new encrypted derivative from an unencrypted source is a supported workflow.",
  "A copy of an encrypted snapshot remains encrypted, and enabled regional encryption-by-default applies to eligible snapshot copies.",
  "Without default encryption or an explicit encryption request, an unencrypted source normally restores to an unencrypted new volume.",
  "The blanket impossibility is false: encryption can be requested for a new restored volume or an encrypted snapshot copy.",
  note="The wording means a new encrypted restore is possible. An already created unencrypted volume cannot be encrypted in place; replace it with an encrypted derivative.")
a(243,"B","ebs","Elastic Volumes can increase the existing EBS volume, followed by the required partition/filesystem expansion.",
  "A new mount point requires more application/storage layout changes than extending the existing volume.",
  "Increase the volume capacity through supported modification and extend the guest partition/filesystem as required.",
  "EBS volume capacity can be increased; the claim that its size is immutable is false.",
  "Snapshot-and-replace is more disruptive than supported live expansion for this requirement.")
a(244,"B","backup","AWS Backup centrally manages supported EFS backup policies, retention, monitoring, and restores.",
  "S3 File Gateway exposes an on-premises storage interface; it is not the central EFS backup-policy service.",
  "AWS Backup supports EFS protection with scheduled plans and retention settings plus central job monitoring.",
  "FSx File Gateway is not a backup manager for EFS and has customer-availability restrictions.",
  "Transfer Acceleration accelerates S3 transfers; it does not provide the requested EFS backup lifecycle.",
  note="Set the actual retention period and test recovery. If immutable retention is required, evaluate appropriate Backup Vault Lock controls separately.")
a(245,"B","efs","Reach existing EFS mount targets over supported routed connectivity instead of duplicating the filesystem.",
  "An EFS filesystem's mount targets are not simultaneously attached to arbitrary multiple VPCs through this proposed operation.",
  "Suitable VPC peering, routes, DNS/mount configuration, and TCP 2049 rules let B reach A's existing mount targets.",
  "EFS is not automatically reachable from every VPC merely because it is in the same Region.",
  "Mount targets live in one VPC, but clients can access them through supported external routed paths.")
h(246,"efs","Options B and C restate the same EFS inbound security-group problem rather than two distinct causes. Peering DNS-resolution flags alone also do not guarantee the EFS mount-target DNS design across Regions; direct reachable mount-target addressing can work. The source does not supply two clearly distinct correct diagnoses.")
a(247,"D","efs","Request TLS while mounting EFS using a supported mount helper or CSI configuration.",
  "Ordinary NFS traffic is not automatically encrypted merely because it uses NFS.",
  "At-rest filesystem settings are not the client mount's in-transit TLS switch.",
  "Transit encryption is configured for the connection/mount; it does not require recreating the filesystem.",
  "The supported EFS mount helper with its TLS option establishes encrypted client-to-filesystem transit.",
  note="Use current efs-utils or the supported CSI settings and optionally enforce secure transport through an appropriate filesystem policy. TLS protocol implementation can evolve beyond the source's exact version wording.")
a(248,"B","efs","General Purpose is the EFS performance mode intended for latency-sensitive ordinary application file access.",
  "Max I/O trades higher per-operation latency for a different scale profile and is not the low-latency choice here.",
  "General Purpose provides the lower-latency performance profile for this web application's file operations.",
  "Bursting is a throughput mode, not the performance-mode choice requested.",
  "Provisioned is also a throughput mode rather than the General Purpose versus Max I/O performance choice.")
a(249,"C","efs","Provisioned throughput decouples the configured throughput from a small filesystem's stored size.",
  "Bursting throughput is tied to the relevant storage-size/credit model and does not promise consistently high throughput for a tiny filesystem.",
  "General Purpose is a performance mode, not the requested independent throughput provisioning choice.",
  "Provisioned mode allows an appropriate explicit throughput amount independent of how little data is stored.",
  "Max I/O is a performance-mode choice and does not directly provide the independent throughput amount described.",
  note="Elastic throughput is a current alternative to evaluate for variable workloads, but it is absent from the offered answers. Measure throughput and size the configured level; no mode abolishes all possible bottlenecks.")
a(251,"D","hooks","A termination lifecycle action can pause an instance while a configured workflow flushes available logs.",
  "Pending:Wait is a launch wait state, not the correct termination wait state.",
  "A workflow can orchestrate collection, but this option does not describe the direct already-agent-based log flush as explicitly as D.",
  "An Instance Terminate Successful event arrives after termination, too late to collect that instance's remaining local files.",
  "The terminate lifecycle action and Terminating:Wait state allow a configured handler to flush agent logs before completing the hook.",
  note="For the easiest robust ongoing solution, stream logs continuously with a configured CloudWatch agent before failure. A last-minute hook is best-effort and cannot recover logs from an unreachable host; it is only the best specific hook/event pairing offered.")
a(252,"D","s3endpoint","An S3 gateway endpoint avoids a NAT instance for eligible same-Region S3 traffic.",
  "An S3 interface endpoint can provide private connectivity but has endpoint-hour/data charges unnecessary for this VPC-local gateway use case.",
  "A NAT gateway remains a paid general-egress path rather than the lowest-cost dedicated S3 endpoint option.",
  "A smaller NAT instance retains host management, availability concerns, and instance costs.",
  "A gateway endpoint provides eligible S3 access without gateway-endpoint hourly/data-processing charges.",
  note="Retain other necessary internet paths if the instance also uses non-S3 services. Endpoint, bucket, and identity policies still apply.")
a(253,"CD","eks","Scale pod replicas for workload demand and node capacity for unschedulable supported workloads.",
  "Vertical Pod Autoscaler changes pod resource requests, not the required horizontal replica/node scaling combination.",
  "Karpenter is a valid modern node-scaling tool when correctly configured for pending/unschedulable demand; this option's generic failed/rescheduled-pod description does not specify that valid trigger.",
  "HPA can scale replica counts based on supported metrics when the metrics pipeline is configured.",
  "Cluster Autoscaler adjusts suitable node groups for scheduling demand, complementing pod replica scaling.",
  "CloudWatch alarms alone do not implement the Kubernetes pod-and-node autoscaling mechanisms described.",
  note="Karpenter or EKS Auto Mode can be appropriate alternatives to Cluster Autoscaler; do not memorise 'Karpenter is wrong'. The source's B description is incomplete, while C+D is the explicit complete pair offered.")
a(254,"D","tracking","Step scaling applies different capacity adjustments according to how far an alarm metric breaches a threshold.",
  "Simple scaling applies its configured adjustment with cooldown behaviour rather than a set of breach-sized adjustment steps.",
  "Target tracking asks AWS to maintain a desired metric target rather than defining the described adjustment steps directly.",
  "Scheduled scaling changes capacity at planned times rather than reacting to these metric-threshold breaches.",
  "Step scaling uses configured metric/alarm thresholds and adjustment ranges to select the capacity change.")
h(255,"alb","ALB access logs are the right request-level evidence, but delivery is best-effort rather than a complete guaranteed record every five minutes. The attached CloudWatch Application Insights claim also does not establish supported analysis of all ECS Anywhere request logs. None of the offered complete combinations satisfies all of the source's absolute logging/integration claims.")
a(258,"C","sqs","Visibility timeout hides a received message while a consumer processes it.",
  "Component Timeout is not the SQS message-hiding setting.",
  "Processing Timeout is not the name of the SQS visibility control.",
  "Visibility timeout temporarily hides received messages; successful consumers must delete them before they reappear.",
  "Receiving Timeout is not the message-visibility setting described here.")
a(259,"B","as","Tune the scaling policy's stabilisation and thresholds to avoid reacting repeatedly before capacity settles.",
  "Larger instances do not directly correct an oscillating threshold/cooldown policy and may increase cost.",
  "Appropriate cooldown/warm-up and threshold tuning can reduce oscillating scaling decisions while preserving demand-based scaling.",
  "Provisioned IOPS affects EBS storage performance rather than the group's scaling decision stabilisation.",
  "More baseline instances can increase cost without correcting the oscillation mechanism.",
  note="Cooldown, instance warm-up, metric aggregation, and target tracking behave differently. Do not blindly raise thresholds; measure the cause and retain the required response time.")
a(260,"A","spot","Use commitment discounts for a suitable predictable non-interruptible baseline and Spot for interruptible work.",
  "The mixed purchasing strategy matches stable important work with discounted baseline capacity and flexible jobs with interruptible capacity.",
  "Reserving all capacity may pay for unused commitments where non-essential jobs could exploit cheaper spare capacity.",
  "All On-Demand avoids commitments but does not use either offered discount opportunity.",
  "Putting every critical uninterruptible job on Spot ignores the potential capacity interruption.",
  note="This assumes the baseline is predictable over the commitment and non-essential jobs tolerate interruption. RIs are primarily billing constructs; capacity and job placement must be designed separately.")
a(261,"D","kinesis","A retained Kinesis stream supports live consumers and replay of the last twelve hours.",
  "CloudTrail records supported AWS activity; it does not ingest arbitrary application log streams as a general custom-log pipeline.",
  "S3 and an EMR pipeline can support analytics but do not express the requested low-overhead retained live stream as directly.",
  "Consumed/deleted SQS work is not a replayable journal available to a future independent heuristic validator.",
  "Kinesis Data Streams can retain log events while independent consumers apply heuristics and reread the required window.",
  note="Set sufficient retention, partition distribution, and consumer capacity. Replay is limited to records still retained.")
a(262,"A","appsync","AppSync provides managed GraphQL APIs with supported custom domains and ACM certificates.",
  "AppSync directly supplies the requested serverless GraphQL interface and supported custom-domain HTTPS integration.",
  "The proposed Outposts/Anywhere/Fargate combination is not the simple supported managed GraphQL/custom-domain solution.",
  "DNSSEC authenticates DNS data; it does not create HTTPS/TLS protection for a Beanstalk API.",
  "Directory controllers do not enable this VMware GraphQL API's TLS/custom-domain integration.")
a(263,"A","trail","Configure CloudTrail to capture the required supported management and data events and deliver them durably.",
  "An appropriately configured trail records the supported API/activity events and can deliver encrypted records to S3.",
  "API Gateway logs calls through an API, not all of the EC2 SDK's direct calls to other AWS services.",
  "CloudWatch metrics/logs do not automatically capture the required full supported AWS API audit trail.",
  "Distributed tracing follows instrumented application requests; it is not a replacement for CloudTrail audit capture.",
  note="Not literally every AWS API is logged in every mode. Configure required data events, Regions, accounts, retention, integrity validation, and immutability where needed.")
a(264,"AB","waf","Evaluate the approved-IP allow rule before the country-block rule in the WAF web ACL.",
  "A geo-match block rule can reject requests from the specified country after authorised exceptions have been evaluated.",
  "A higher-priority terminating allow rule for the approved IP set can make the requested exceptions.",
  "An ALB listener allow does not override a WAF request that has already been blocked.",
  "ALB listener routing is not the native country geo-match web ACL control.",
  "NACLs are CIDR/protocol controls, not a managed WAF-style request geolocation rule, and TGW placement does not change that.",
  note="Rule order matters: an earlier terminating country block would stop the later allow from running. Interpret forwarded client IPs correctly when proxies are involved.")
a(265,"C","eks","Run supported EKS EC2 worker nodes in Wavelength Zones for carrier-edge placement.",
  "A VPC endpoint is not the mechanism for creating an EKS worker node's Wavelength placement.",
  "A Fargate profile and EC2 node-group roles are different constructs; the proposed combined role/placement claim is unsupported.",
  "Supported EKS worker node groups in Wavelength Zones provide carrier-edge compute with the required configured cluster authentication.",
  "An EKS connector-agent role and Control Tower do not supply the claimed in-cluster RBAC authentication design.",
  note="The source uses historical aws-auth ConfigMap management; prefer supported EKS access entries when appropriate. Wavelength placement alone does not guarantee every application request meets a latency target.")
a(266,"AB","peering","Inter-Region peering needs accepted connectivity and reciprocal route entries for the remote networks.",
  "VPC peering supports appropriate private connectivity between non-overlapping VPCs in different Regions.",
  "Subnet route tables must send the intended remote destinations through the accepted peering connection.",
  "An egress-only gateway handles supported IPv6 internet initiation, not this direct VPC-to-VPC private route.",
  "NAT gateways do not directly connect arbitrary VPCs across Regions.",
  "Generic service VPC endpoints do not provide full routed connectivity between these two instance networks.",
  note="Security groups, NACLs, and DNS must also permit the intended communication. A peering connection alone is not a complete access policy.")
a(267,"A","gateway","Cached Volume Gateway keeps primary data in AWS while caching frequently accessed blocks locally.",
  "Cached volumes extend on-premises capacity through supported cloud-backed iSCSI storage with a local working-set cache.",
  "Remote EC2/EBS storage does not by itself provide the on-premises local-cache interface described.",
  "ElastiCache is not the on-premises block-storage cache appliance for these existing applications.",
  "An archive service does not provide low-latency working-set access for this hybrid volume requirement.",
  note="Cached Volume Gateway exposes block volumes, not ordinary directly browsable S3 objects; choose File Gateway instead if the actual requirement is native S3 objects through file shares.")
a(268,"C","appsync","AppSync pipeline resolvers can sequence supported data-source operations behind a GraphQL API.",
  "CloudFront Functions are constrained edge scripts, not a general cross-table DynamoDB data-access workflow.",
  "A custom Lambda API can work, but needs additional handler code where supported pipeline resolvers fit the access pattern.",
  "Pipeline resolvers can coordinate supported operations across the required data sources with managed GraphQL integration.",
  "Athena federation targets analytics queries rather than the application's ordinary low-latency read/write API.",
  note="A pipeline is not automatically atomic across tables. Use supported transactions and capacity design when atomicity or strict performance guarantees are required.")
a(269,"B","vpc","A subnet NACL can explicitly deny the known malicious source IPs; security groups cannot add deny rules.",
  "Changing entry addresses does not block the identified sources or repair the administrative exposure.",
  "An appropriately ordered NACL deny rule can immediately block matching known source CIDRs.",
  "Moving an existing instance between subnets is not an in-place operation and is more disruptive than the requested temporary block.",
  "Removing the IGW disrupts legitimate internet connectivity for the VPC rather than targeting only the attackers.",
  note="WAF does not inspect SSH, and GuardDuty detects rather than patches this exposure. Long-term controls include restricted administrative sources and supported Session Manager/VPN access.")
a(270,"A","s3endpoint","Use an S3 gateway endpoint for eligible VPC-local S3 traffic instead of paying for NAT processing.",
  "The gateway endpoint routes eligible S3 traffic privately without its own hourly/data-processing fee.",
  "A managed NAT gateway does not expose an EC2 instance size to downsize.",
  "Transit Gateway is not a per-bucket S3 service endpoint or a necessary layer for this local access.",
  "A NAT instance introduces host operations and potential availability limitations while retaining compute cost.",
  note="Retain a NAT path if other dependencies still need general internet access; do not delete unrelated egress requirements blindly.")
a(271,"C","waf","Network Firewall is an inline VPC traffic-inspection control when the routes direct traffic through its endpoints.",
  "Network Access Analyzer evaluates network access configurations; it is not an inline inspection engine for every packet.",
  "The proposal does not establish a supported NLB traffic-mirror source/interface design and confuses mirroring with inline filtering.",
  "Network Firewall with suitable rules, endpoints, and routing can inspect supported ingress/egress flows.",
  "Detective investigates security activity; Reachability Analyzer evaluates paths rather than deploying an inline subnet firewall.")
a(272,"A","ssm","Systems Manager Run Command executes supported fleet commands without opening SSH or RDP sessions.",
  "Managed instances can run authorised commands through SSM Agent and appropriate service connectivity.",
  "CodePipeline coordinates delivery pipelines, not the direct managed-instance command capability named here.",
  "EC2Config is a legacy Windows instance component rather than the general current fleet command solution.",
  "AWS Config records/evaluates resource configurations rather than distributing arbitrary operating-system commands.")
a(273,"B","ad","WorkSpaces supplies virtual desktops; Directory Service and hybrid networking support the identity/network requirements.",
  "IAM supplies AWS permissions but is not the actual managed virtual-desktop product requested.",
  "An appropriate WorkSpaces, directory, and VPN configuration provides managed desktops with supported hybrid access.",
  "ClassicLink is obsolete and is not the requested desktop service.",
  "S3 stores objects and does not provide the users' Windows/Linux desktop sessions.",
  note="Choose a supported directory integration such as appropriate AD Connector/Managed AD for the actual WorkSpaces configuration; check licensing and network requirements.")
a(274,"D","waf","WAF geo-match rules block supported HTTP requests by country at the ALB layer.",
  "A manually maintained NACL IP list is operationally heavy and does not directly implement country geolocation matching.",
  "Instance-subnet NACLs have the same CIDR-list maintenance problem and are not HTTP country rules.",
  "A stateful domain-list rule matches domains, not the origin country of every incoming web user.",
  "A suitable WAF geo-match rule on each supported ALB supplies the requested country-based web access control.",
  note="IP geolocation is not perfect proof of physical user location or regulatory compliance; account for proxies and appropriate forwarded-IP configuration.")
a(275,"BE","kms","EBS encryption uses supported AWS-managed or customer-managed KMS keys.",
  "S3 client-side encryption is an object-upload pattern, not EBS volume encryption.",
  "A suitable customer-managed KMS key can control the supported EBS encryption key hierarchy.",
  "ACM TLS certificates are not the at-rest key-management service used by EBS.",
  "A password stored in CloudHSM is not how EBS selects or uses its supported encryption key.",
  "The AWS-managed EBS KMS key is another supported EBS encryption choice.",
  "S3 server-side object encryption is not the encryption mechanism for an EBS volume.")
a(276,"D","trail","CloudTrail trail log delivery is encrypted by default; customer-managed KMS encryption is an optional additional configuration.",
  "Explicitly setting baseline bucket encryption is not necessary merely to obtain the CloudTrail log encryption already provided by default.",
  "The proposed AES-128 setting is not the stated CloudTrail/S3 default SSE-S3 encryption model.",
  "CloudTrail trails deliver to S3, not directly to a standalone Glacier archive destination.",
  "Delivered trail log files receive default server-side encryption; additional SSE-KMS configuration can meet stronger key-control requirements.",
  note="Create/configure a trail for durable S3 delivery and the required Regions/event categories. Default event history alone is not a custom long-term trail archive.")
h(277,"rds","The generic Amazon RDS choice and Aurora can both provide ACID relational OLTP and complex SQL. Current supported RDS engines can exceed 50 TB, so size alone no longer uniquely selects Aurora. Missing engine compatibility, exact growth target, and performance requirements make the historical storage-limit answer ambiguous.")
a(279,"B","vpn","Use a suitable ECMP-enabled Transit Gateway and multiple dynamic VPN paths for aggregate throughput.",
  "A VPC does not gain this supported ECMP design by attaching multiple virtual private gateways.",
  "Transit Gateway supports appropriate VPN ECMP routing across additional BGP paths/tunnels.",
  "Changing only the customer endpoint may address one device bottleneck but does not establish the required aggregate ECMP architecture.",
  "A generic tunnel-count change omits the supported gateway/routing behaviour needed to use the extra paths.",
  note="ECMP aggregates independent flows; it does not necessarily increase one TCP flow's throughput. Test routing, device capacity, and supported tunnel/attachment quotas.")
a(280,"B","routing","Weighted DNS routing distributes responses according to configured relative weights.",
  "Failover routing chooses primary/secondary health roles rather than a desired concurrent weighted split.",
  "Weighted records assign relative proportions to the two endpoint answers.",
  "Geolocation routes by user location rather than a chosen weighted proportion.",
  "Latency routing selects based on regional latency measurements rather than your desired weight split.",
  note="DNS caching means weights are not a strict guarantee of the exact percentage of individual HTTP requests.")
a(281,"C","dns","A Route 53 A-alias record can point the zone apex at an ALB DNS target.",
  "A standard CNAME cannot be created at the DNS zone apex.",
  "Alias is a supported A/AAAA-style extension here, not a special apex CNAME record.",
  "An A alias targets the supported ALB and tracks its changing endpoint addresses.",
  "Hardcoding a currently observed ALB IP does not follow the ALB's changing addresses.")
a(282,"D","rds","Supported IAM database authentication uses a short-lived signed token and a configured database user.",
  "Secrets Manager manages secrets but is not the mechanism generating IAM DB authentication tokens.",
  "Identity Center workforce sign-in does not alone configure database-native IAM token authentication.",
  "An MFA code is not the RDS MySQL authentication token accepted by the database plugin.",
  "Configure supported IAM DB authentication, the correct database user/plugin, IAM connection permission, and a signed authentication token.",
  note="Use TLS and supported engine/Region settings. A token's short authentication validity does not imply an already established database session expires at that exact time.")
a(286,"C","fsxwindows","Windows SMB/NTFS and AD requirements identify FSx for Windows File Server.",
  "Lustre is a parallel HPC filesystem and does not provide the specified native Windows SMB/NTFS feature set.",
  "Deep Archive is asynchronous archival object storage, not a live Windows shared filesystem.",
  "FSx for Windows File Server provides the supported Windows file-sharing and Active Directory integration features.",
  "DataSync moves data between supported storage services; it is not the destination filesystem itself.")
a(287,"A","ebs","An EBS snapshot can be created while the volume remains in use; application consistency is a separate concern.",
  "The volume can continue normal use during snapshot creation, although application-consistent capture may need quiescing or coordinated flushes.",
  "Snapshot creation does not require making the volume unusable until the snapshot completes.",
  "The volume is not automatically restricted to read-only while its snapshot is being created.",
  "An in-progress snapshot does not impose the blanket attach/detach prohibition claimed here.",
  note="The snapshot captures its point-in-time state, not all later writes until completion. Observe safe filesystem/application shutdown rules when detaching or changing a database.")
a(288,"D","tracking","Step scaling with instance warm-up can react to breach size without repeatedly counting starting instances as capacity ready to serve.",
  "A CDN can help supported cacheable content, but does not directly fix every capacity shortfall for this workload.",
  "Larger instances increase per-instance capacity but do not directly express a responsive scaling/warm-up policy.",
  "Slow start is an ALB target-group feature, not the proposed NLB slow-start setting.",
  "Step adjustments plus an appropriate warm-up interval address scaling response and the instance's readiness delay.",
  note="A known daily spike may be better prepared for with scheduled/predictive scaling, but neither is offered. Warm-up does not eliminate the actual boot time.")
a(290,"C","s3","The listed Glacier archival option can satisfy a 24-hour retrieval allowance more cheaply than hot online storage for suitable access patterns.",
  "Standard-IA provides immediate access but retains a higher storage rate than suitable archival storage.",
  "One Zone-IA weakens resilience for financial data and still targets immediate online retrieval.",
  "A suitable Glacier Flexible Retrieval transition and retrieval tier fits the relaxed archival access deadline among the offered choices.",
  "FSx Windows is a managed live filesystem with costs and features unrelated to this object-archive requirement.",
  note="Interpret historical 'Glacier' as Flexible Retrieval. Model storage duration and retrieval volume/cost; Deep Archive is another modern candidate but is absent from these choices. A day-zero transition is supported for eligible objects.")
a(291,"B","s3","Among these options, Standard-IA fits known infrequent access with immediate retrieval and multi-AZ durability.",
  "Standard meets retrieval timing but uses a hotter storage price profile than the stated rare access needs.",
  "Standard-IA provides millisecond retrieval and regional durability for suitable infrequently read objects.",
  "Deep Archive requires asynchronous restore and fails the surprise-audit immediate retrieval requirement.",
  "Intelligent-Tiering fits uncertain/changing patterns; the question supplies a known quarterly access pattern, so it is not the strongest listed fit.",
  note="Glacier Instant Retrieval is a modern archival alternative absent from the options. Include object size, monitoring, retention, and retrieval charges in an actual cost comparison.")
a(292,"B","dms","Convert heterogeneous schema/code, resolve incompatibilities, then migrate supported data with DMS.",
  "Neptune is a graph database and Batch is not the native schema-conversion/database-CDC toolchain.",
  "SCT supplies supported schema/code conversion assessment and DMS moves supported source data and changes.",
  "AWS supports suitable heterogeneous database migrations; they do not require this blanket out-of-AWS conversion restriction.",
  "An EC2 launch template configures instances; it does not automatically translate Oracle schema and application code.",
  note="Automated conversion is not complete for every schema feature or stored program. Review conversion action items and validate the application on PostgreSQL.")
a(293,"D","objectlock","Bulk-copy objects with DataSync; use S3 data events for object access auditing and Object Lock for supported version retention.",
  "A gateway is primarily an ongoing hybrid access interface, and management events alone do not audit object reads/writes.",
  "DataSync is suitable for migration, but management-only events miss the requested object access audit trail.",
  "An EC2/EBS destination does not gain S3 Object Lock by naming a separate bucket's access logs.",
  "DataSync moves supported files, while configured S3 data events capture object operations and Object Lock protects retained versions.",
  note="Indefinite retention needs an appropriate legal-hold/retention process and authorisation controls; Object Lock alone is not automatic perpetual immutability. Include management events, all required data-event selectors, and permissions for the full audit scope.")
a(294,"A","lambda","A small bounded daily processing job is a natural pay-per-invocation Lambda workload.",
  "A suitable 512 MB Lambda function can process the small object without an always-running server or warehouse.",
  "A PySpark ETL job adds unnecessary startup and compute infrastructure for this tiny bounded processing task.",
  "A warehouse and another ingestion path add cost and complexity when the data is already in S3.",
  "A continuously available EC2 processor and delivery service add resources not needed for the small daily workload.",
  note="Benchmark the ten-second target with the actual code and dependencies. Selecting Lambda alone does not guarantee an arbitrary workload's runtime.")
a(295,"AC","macie","Macie detects supported sensitive S3 content; EventBridge and SNS distribute matching findings as notifications.",
  "An appropriate EventBridge rule can send relevant Macie findings to an SNS notification topic.",
  "An IoT broker is not the direct managed operations-notification target needed here, and the event naming is not reliable.",
  "Macie can discover supported sensitive content; match the current Macie Finding event structure in EventBridge.",
  "SQS stores work for consumers rather than directly supplying the operations notification channel described.",
  "GuardDuty threat findings are not a replacement for Macie's object-content classification.",
  prompt="A company discovers that PII was mistakenly uploaded to S3. It wants ongoing sensitive-data discovery and notifications when relevant findings recur, so staff can remediate them. Which two offered components provide this detection-and-notification workflow?",
  note="Editorial clarification: this is detection/notification, not a guarantee of preventing uploads. The historical event label is replaced in the explanation by current Macie Finding/EventBridge matching; remediation and preventive controls need separate design.")
a(296,"C","batch","AWS Batch manages suitable queued parallel jobs and compute placement for long-running simulations.",
  "Spot can reduce interruptible compute cost, but instances alone do not provide managed job scheduling and execution.",
  "An indivisible simulation lasting hours exceeds Lambda's 15-minute invocation limit and the stated resource profile.",
  "Batch schedules and runs suitable containerised simulations on configured compute environments with less custom orchestration.",
  "Fargate is a compute option with resource limits, not the complete high-resource managed batch-scheduling solution described.",
  note="Package and parallelise the simulation appropriately; Batch does not automatically rewrite a serial algorithm to use many nodes. Select a compute environment meeting its actual memory/CPU needs.")
a(297,"C","s3endpoint","A suitable S3 gateway endpoint routes private VPC-to-S3 traffic without a public internet egress path.",
  "Transit Gateway provides routed network connectivity, not the native per-service S3 endpoint on its own.",
  "A NAT gateway in a private subnet is not the correct public-NAT internet path and does not supply the endpoint design.",
  "An S3 gateway endpoint with suitable route tables/policies meets the private service-access requirement.",
  "An IGW is attached to a VPC, not placed in a subnet, and is not the desired private endpoint mechanism.")
a(298,"A","iam","Use appropriate resource tags and IAM conditions for supported environment-specific EC2 operations.",
  "A suitable IAM condition can scope supported actions to UAT-tagged resources while withholding production permissions.",
  "VPC network separation does not by itself restrict which EC2 management API operations a user can perform.",
  "AZ separation and MFA do not express resource-specific permission boundaries between UAT and production.",
  "RAM shares supported resources; it is not the primary identity policy mechanism for these EC2 management permissions.",
  note="Protect the environment tags from unauthorised changes and check each action's resource/condition support. Separate AWS accounts provide a stronger isolation boundary for many production designs.")
a(299,"D","glue","Glue supplies managed ETL jobs; S3 events and Lambda can trigger a suitable job workflow.",
  "S3 Select is a limited historical object-query feature, not a general managed ETL engine, and is closed to new customers.",
  "Spectrum queries external data from Redshift rather than acting as the ETL transformation job service.",
  "Step Functions orchestrates tasks but is not itself the data-transformation compute engine.",
  "Glue provides managed supported extraction/transformation/loading jobs that a suitable event handler can start.")
a(300,"B","vpn","Direct Connect supplies supported dedicated private hybrid connectivity with consistent bandwidth characteristics.",
  "A normal Site-to-Site VPN is an encrypted internet path rather than the requested dedicated circuit.",
  "Direct Connect provides dedicated connectivity from a suitable customer/partner location to AWS.",
  "TGW ECMP can aggregate supported VPN paths but does not turn internet paths into a dedicated physical connection.",
  "A transit VPC is a network architecture, not a dedicated hybrid connectivity product by itself.",
  note="Plan redundant connections and encryption if required; private connectivity alone is not an encryption guarantee.")
a(301,"D","s3","The stated request rates are below S3's documented per-prefix baseline; old mandatory random-prefix advice is unnecessary.",
  "Sequential/date keys can be useful for organisation but are not required to unlock these already supported request rates.",
  "Range GETs retrieve object portions and do not directly address the total PUT/GET request rate in the question.",
  "Randomised prefixes are not mandatory at the stated below-baseline request rate.",
  "S3 supports at least 3,500 write and 5,500 GET/HEAD requests per second per partitioned prefix, above these stated rates.",
  note="Scale testing and retries still matter; sudden scaling and workloads can see transient 503s. The answer is not a claim of unlimited instantaneous throughput without design.")
a(302,"C","gateway","Cached Volume Gateway exposes iSCSI storage backed by AWS while keeping a local working-set cache.",
  "Tape Gateway exposes virtual tape devices, not the application's ordinary cloud-backed iSCSI data volume.",
  "File Gateway exposes supported file shares rather than the required block-volume iSCSI interface.",
  "Cached mode reduces the required full local dataset capacity while caching frequently used blocks.",
  "Stored mode keeps the full primary dataset locally and therefore does not minimise local storage expansion as requested.")
a(303,"D","sqs","SQS default retention is four days, so weekly processing can miss messages that have already expired.",
  "Missing permissions would prevent access rather than explain expiration of older queued messages on a weekly cadence.",
  "Short polling can affect receive behaviour but does not change the queue's four-day default retention.",
  "Long polling does not delete messages solely because a weekly consumer waits too long to run.",
  "Messages exceeding the configured retention are removed automatically; the default is shorter than the weekly processing interval.",
  note="Set suitable retention (up to 14 days), process more frequently, and use durable storage for longer-term work records.")
h(304,"kms","The source describes legacy CloudHSM zeroisation after three administrator login failures. Current CloudHSM credential lockout, backup, and recovery behaviour differs, including automatically managed cluster backups. Without a supported current HSM/version and backup state, the claim that no key copy can exist or that a generic snapshot restores it is unreliable historical material.")
a(305,"AD","routing","Weighted DNS answers or ALB weighted target groups can stage traffic across supported AWS/on-premises targets.",
  "Weighted Route 53 records can gradually shift traffic between reachable endpoint sets using configured relative weights.",
  "Global Accelerator cannot directly target arbitrary on-premises endpoints merely by assigning an anycast IP to that network.",
  "Failover routing selects primary/secondary health roles, not a concurrent 50/50 distribution.",
  "An ALB can forward to weighted target groups with supported AWS and reachable on-premises private-IP targets.",
  "NLB does not offer the ALB listener's weighted target-group forwarding action described here.",
  note="Neither DNS weights nor routing changes alone guarantee exact per-request percentages or zero-downtime migration. Design health checks, sessions, shared data, connectivity, and rollback.")
a(306,"AB","ebs","Encrypted EBS covers its volume-to-instance data path and snapshots derived from the encrypted volume.",
  "The supported EBS encryption path encrypts data moving between an encrypted volume and the instance.",
  "Snapshots created from the encrypted EBS volume are encrypted automatically.",
  "Volumes created from encrypted snapshots remain encrypted rather than becoming plaintext.",
  "This incorrectly excludes the volume-to-instance encryption protection provided by EBS encryption.",
  "This contradicts the inherited encryption of snapshots derived from encrypted volumes.")
a(307,"CE","kinesis","Stream consumers can write processed results to suitable durable destinations such as Redshift or S3.",
  "Glue is a data integration/catalogue service, not the ordinary result datastore named by these choices.",
  "Glacier Select was a query feature, not a generic result-storage destination.",
  "A consumer can load appropriate processed analytical results into Redshift through a suitable supported ingestion path.",
  "Athena is a query service; its underlying result files normally reside in a storage service such as S3.",
  "A consumer can persist output objects in S3 with appropriate permissions and batching/formatting.",
  note="These are possible destinations, not a requirement to write every individual record synchronously into a warehouse.")
a(308,"B","efa","t3a supports ENA enhanced networking; do not choose an unsupported EFA or legacy Intel VF combination.",
  "The legacy Intel 82599 VF driver is not the enhanced-networking interface for the stated t3a instances.",
  "ENA is the supported enhanced-networking interface for t3a and supplies the relevant supported network capabilities.",
  "The proposed Windows t3a.medium configuration is not an appropriate supported EFA deployment.",
  "ParallelCluster does not automatically give an unsupported instance/OS combination the requested network hardware capability.",
  note="ENA is already enabled on supported current images/types; this does not mean a missing toggle alone explains performance. t3a.medium is not generally an ideal tightly coupled CFD instance family.")
a(309,"B","fsxwindows","Use FSx for Windows File Server for native Windows shared files with AD integration.",
  "EFS is an NFS service and does not provide the stated Windows SMB/AD filesystem feature set.",
  "FSx for Windows File Server provides native Windows shared-filesystem capabilities and supported Active Directory integration.",
  "File Gateway provides a hybrid file/object interface, not the same native Windows filesystem feature set requested.",
  "An EBS volume is AZ-local block storage rather than a managed Windows shared-filesystem service.")
h(310,"s3endpoint","An S3 gateway endpoint can make the private EC2-to-S3 leg private, but internet users following presigned S3 URLs still contact S3 directly over their own network path. None of the choices supplies a private viewer path or an application proxy architecture. Adding a VPC endpoint alone does not fix the stated concern about all users' internet access.")
a(312,"B","auroraha","Without an Aurora Replica, there is no existing reader to promote; Aurora must recreate writer compute.",
  "This does not match the documented same-AZ recreation behaviour described for a single-instance Aurora cluster.",
  "For a single-instance cluster without a replica, Aurora attempts best-effort recreation in the original AZ; adding replicas improves recovery options.",
  "The source explicitly has no healthy replica, so promotion of an existing replica is unavailable.",
  "Changing the DNS record terminology does not create a nonexistent replica to promote.",
  note="Aurora storage remains distributed independently of the lone compute instance. For stronger availability, configure supported Aurora Replicas in suitable AZs and test recovery.")
a(313,"B","alb","An open HTTP port does not prove that the load balancer's health check reaches a valid responding application path.",
  "An unsuitable AMI can break an application, but the most direct offered health-status configuration diagnosis is the health check.",
  "Wrong path, port, protocol, expected code, or timing can mark targets unhealthy even when TCP port 80 is allowed.",
  "A network path can matter, but the source does not establish that the subnet is wrong merely from the health result.",
  "An instance type alone does not normally determine whether the configured HTTP health endpoint returns the expected response.",
  note="Check actual target health reason codes, application responses, security groups, NACLs, and routes. This is a likely diagnosis among the choices, not proof that all other failure causes are impossible.")

# Specific verification pages where the original collection's shared doc key was too broad.
for index, docs in {
    130: ["redshiftshare"], 168: ["optimizer", "securityhub"],
    173: ["outposts"], 186: ["cloudhsmstore", "rds"],
    233: ["dx"], 300: ["dx"],
}.items():
    REVIEWS[index]["docs"] = docs
