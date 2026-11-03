"""Reviewed prose repairs, applied after answer decisions and duplicate grouping.

The local spelling/grammar tools only supplied flags. Rules below are explicitly
reviewed; identifiers are protected and field-specific repairs preserve distractors.
The generated ledger records every before/after value for source comparison.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEWED_AT = "2026-11-03"

# Unambiguous OCR words, reviewed against the surrounding question/explanation.
WORDS = {
    "nith":"with", "Wth":"with", "Wthin":"within", "applicaton":"application",
    "Applicaton":"Application", "applicatons":"applications", "Confgure":"Configure",
    "confgure":"configure", "customi":"custom", "customi-":"custom-",
    "teami":"team", "dentities":"identities", "profles":"profiles",
    "occurrinc":"occurring", "dlmensions":"dimensions", "argets":"targets",
    "rece":"receive", "alarrns":"alarms", "rernoved":"removed", "tirnes":"times",
    "auditois":"auditors", "enctyption":"encryption", "ctyptographically":"cryptographically",
    "implernent":"implement", "nrrite":"write", "reccwery":"recovery",
    "remcwes":"removes", "ennpty":"empty", "annount":"amount", "connponents":"components",
    "systemi":"system", "managennent":"management", "streaml":"stream",
    "infrastructura":"infrastructure", "kepvords":"keywords", "instancee":"instances",
    "anomaliee":"anomalies", "mitigatione":"mitigations", "capabilitiee":"capabilities",
    "messagee":"messages", "replicae":"replicas", "subnete":"subnets", "databas":"database",
    "uploade":"uploads", "usefs":"users", "WI-ich":"Which", "opt-on":"option",
    "except-on":"exception", "per-od":"period", "spec-al":"special",
    "follow-ng":"following", "automat-cally":"automatically", "not-ce":"notice",
    "forw'ard":"forward", "Appl'cation":"Application", "appl'cation":"application",
    "appl'caton":"application", "ava'lable":"available", "serv'ers":"servers",
    "repl'caton":"replication", "Repl'caton":"Replication", "lowAatency":"low-latency",
    "lowrmaintenance":"low-maintenance", "latencrsensitive":"latency-sensitive",
    "latencrbased":"latency-based", "Wndows":"Windows", "Wldlife":"Wildlife",
    "Neuork":"Network", "Piace":"Place", "Reprcate":"Replicate", "MySQ":"MySQL",
    "Arehose":"Firehose", "MylSAM":"MyISAM", "dont":"don't", "doesnt":"doesn't",
    "cant":"cannot", "Whats":"What's", "everytime":"every time",
    "Requestthe":"Request the", "Aska":"Ask a", "Createa":"Create a", "usea":"use a",
    "builda":"build a", "Adda":"Add a", "Launcha":"Launch a", "centerto":"center to",
    "to a a":"to a", "entify":"Identify", "loy":"Deploy", "licate":"Replicate",
    "ify":"Modify", "cify":"Specify", "licences":"licenses",
    "Sa":"S3", "S30ne":"S3 One", "lops":"IOPS", "APl":"API", "CLl":"CLI",
    "lGW":"IGW", "ldP":"IdP", "ldPs":"IdPs", "PCl":"PCI", "D8":"DB",
    "ntelligent-Tiering":"Intelligent-Tiering",
    "profes":"profiles", "pur":"your", "latenc":"latency", "btency":"latency",
    "reprcas":"replicas", "capac":"capacity", "nterface":"interface", "compliances":"compliance",
    "neüorking":"networking", "neü":"network", "Tinge":"range", "traversaL":"traversal",
    "neüork":"network",
    "sacrific-ng":"sacrificing", "Window.rs":"Windows", "visualises":"visualizes",
    "parallelise":"parallelize",
    "gracefu":"graceful", "orthe":"or the", "toa":"to a", "Sg":"S3",
}
AMERICAN = {
    "behaviour":"behavior", "authorised":"authorized", "authorisation":"authorization",
    "authorise":"authorize", "authorises":"authorizes", "unauthorised":"unauthorized",
    "synchronisation":"synchronization", "synchronise":"synchronize",
    "initialised":"initialized", "initialisation":"initialization", "reinitialisation":"reinitialization",
    "analyse":"analyze", "optimise":"optimize", "optimised":"optimized",
    "minimise":"minimize", "organisation":"organization", "centralises":"centralizes",
    "centralising":"centralizing", "centralised":"centralized", "containerised":"containerized",
    "catalogue":"catalog", "fulfilment":"fulfillment", "artefacts":"artifacts",
    "customise":"customize", "favours":"favors", "synthesising":"synthesizing",
    "synthesises":"synthesizes", "utilisation":"utilization", "specialised":"specialized",
    "enquiries":"inquiries", "travelling":"traveling", "stabilisation":"stabilization",
    "memorise":"memorize", "recognising":"recognizing", "randomised":"randomized",
    "centre":"center", "afterwards":"afterward",
    "visualise":"visualize", "visualises":"visualizes", "visualised":"visualized",
    "analysed":"analyzed", "analysing":"analyzing", "optimisation":"optimization",
    "recognised":"recognized", "categorised":"categorized", "synchronised":"synchronized",
}
PHRASES = {
    '"\'"thout':"without", "'\"thout":"without", '"thout':"without",
    "cost effic ency":"cost efficiency", "data-such as":"data, such as",
    "Rekognition s":"Rekognition's", "spec-es":"species", "theVve":"they have",
    "'dentities":"identities", "(PID":"(PII)", "(PBO":"(PBK)", "(KP )":"(KPL)",
    "(AC )":"(ACL)", "(EN )":"(ENI)", "betw.'een":"between", "betw een":"between",
    "beh' nd":"behind", "public-fac' ng":"public-facing", "tool' ng":"tooling",
    "opt' mization":"optimization", "ava' lability":"availability", "ofl":"of",
    "afterw ard":"afterward", "rece ving":"receiving", "mon toring":"monitoring",
    "netw orking":"networking", "netu orking":"networking", "comput ng":"computing",
    "sacrific- ing":"sacrificing", "pr vate":"private", "latenc y":"latency",
    "üo-tier":"two-tier", "key/value":"key-value", "kervalue":"key-value",
    "gracefu l":"graceful", "Provi sioned":"Provisioned", "Ser.'erless":"Serverless",
    "ConfiguretheS3":"Configure the S3", "ConfguretheS3":"Configure the S3",
    "Sastatic":"as static", "stream' live":"stream live", "a -timeout\" error":'a "timeout" error',
    "Cloudwatch":"CloudWatch", "Cloudwatch Logs":"CloudWatch Logs", "Elasticache":"ElastiCache",
    "AWSConfig":"AWS Config", "AWSAppFlow":"AWS AppFlow", "ECSFargate":"ECS Fargate",
    "Datasync":"DataSync", "QuickSght":"QuickSight", "Webp":"WebP", "Javascript":"JavaScript",
    "Codepipeline":"CodePipeline", "CodePipeLine":"CodePipeline", "ParallelCLuster":"ParallelCluster",
    "Workspaces":"WorkSpaces", "Point-ln-Time":"Point-in-Time", "Mufti-Availability":"Multi-Availability",
    "Standard-lA":"Standard-IA", "One-Zone-lA":"One Zone-IA", "Saone":"S3 One",
    "privateLink":"PrivateLink",
    "lnvokeFunction":"InvokeFunction", "taskRoLeArn":"taskRoleArn", "EnableTasklAMRoLe":"EnableTaskIAMRole",
    "CPUUtiLization":"CPUUtilization", "SwapUtiLization":"SwapUtilization",
    "ClosestToNextlnstanceHour":"ClosestToNextInstanceHour", "Oldestlnstance":"OldestInstance",
    "CreateVoLume":"CreateVolume", "CopySnapshotAndUpdateVoLume":"CopySnapshotAndUpdateVolume",
    "Opsltem":"OpsItem", "Deletionpolicy":"DeletionPolicy", "CopySnapshotAndUpdateVolume":"CopySnapshotAndUpdateVolume",
    "low number of":"small number of", "a few number of":"a small number of",
    "independently from the Life":"independently of the lifetime", "Meta Data":"metadata",
    "user name":"username", "micro-services":"microservices", "micro-service":"microservice",
    "on-going":"ongoing", "on-premise ":"on-premises ", "pre-signed":"presigned",
    "Comprehend analyses":"Comprehend analyzes", "Rekognition analyses":"Rekognition analyzes",
    "S-31ntelligent-Tiering":"S3 Intelligent-Tiering", "S3Standard":"S3 Standard",
    "SaGateway":"S3 gateway", "1/0":"I/O", "Artificial Intelligence (Al)":"artificial intelligence (AI)",
    "Al-powered":"AI-powered", "Multi Factor Authentication":"multi-factor authentication",
    "EFS Max 1/0":"EFS Max I/O", "e.g„":"e.g.,", "lifecße":"lifecycle",
    "HDD(sc1)":"HDD (sc1)", "HDD(st1)":"HDD (st1)", "HDD(scl)":"HDD (sc1)",
    "aggregation_dlmensions":"aggregation_dimensions", "sacrific-ng":"sacrificing",
    "netw. orking":"networking", "neüorking":"networking", "comput.ng":"computing",
    "netw ork":"network", "netw.ork":"network", "afterw.ard":"afterward",
    "gracefu.l":"graceful", "pr.ediction":"prediction", "awssourcevpc'":"aws:SourceVpc",
    "aws:sourcevpce":"aws:SourceVpce",
    "effic ency":"efficiency", "p ediction":"prediction", "letc/ecs/ecs.config":"/etc/ecs/ecs.config",
    "capacity ty":"capacity", "S31nterface":"S3 interface", "source 'P":"source IP",
    "API analyses":"API analyzes", "S30bject/PersonaL":"S3Object/Personal",
    "pretrained":"pre-trained", "sub-domains":"subdomains", "mixed instances policy":"mixed-instances policy",
    "the viable listed network cause":"a plausible network cause among the listed options",
    "plausible listed cause":"plausible cause among the listed options",
    "possible listed cause":"possible cause among the listed options",
    "the direct listed fix":"the most direct fix among the listed options",
    "the appropriate offered control":"the most direct control among the listed options",
    "N.Virginia":"N. Virginia", "Global Accelerator accelerator":"Global Accelerator",
    "to backup":"to back up", "directly backup":"directly back up", "ie. production":"i.e. production",
    "highly-scalable":"highly scalable", "highly-available":"highly available", "fully-managed":"fully managed",
    "querrstring":"query-string", "cach- ing":"caching", "pr ediction":"prediction",
}

# Complete field rewrites where punctuation alone would conceal a dropped word or list.
FIELDS = {
    1: {"prompt":"You have deployed an e-commerce website on Amazon EC2 instances behind an Application Load Balancer (ALB). Its domain is myshoppingweb.com. Customers must be able to access both myshoppingweb.com (the root domain) and www.myshoppingweb.com (the subdomain). DNS is managed in Amazon Route 53. Which Route 53 configuration meets this requirement?",
        "options.0":"Create a CNAME record for myshoppingweb.com pointing to the ALB and an alias record for www.myshoppingweb.com pointing to the ALB.",
        "options.1":"Create CNAME records for both myshoppingweb.com and www.myshoppingweb.com."},
    13: {"prompt":"A financial services company stores customer data in multiple Amazon S3 buckets. An internal audit discovers that some customer-uploaded files contain personally identifiable information (PII). The head of operations wants to automatically scan all the buckets, detect sensitive data using predefined patterns, and generate findings for compliance audits. Which service should a solutions architect recommend?"},
    34: {"prompt":"A startup's DevOps team is slow to detect and investigate problems. A security audit finds sensitive values, such as configuration variables, product keys, and AMI IDs, hardcoded in application code. The CIO wants faster failure analysis and secure secret storage. Automated rotation is not required, and cost efficiency matters. Which actions should the team take?"},
    52: {"prompt":"A media company sells stock images and videos. Users access the content through URLs. Access must be limited to customers who purchased the content, without changing the original URL for each access. Which mechanism should the company use?"},
    54: {"prompt":"Account A stores unencrypted manual Amazon RDS snapshots in us-east-1. It must share them with specific AWS accounts in the same Region. How should it do this?",
         "options.0":"In Account A, keep the manual DB snapshot private and share it with the specified accounts. In those accounts, restore DB instances directly from the shared snapshot."},
    110: {"prompt":"A web application runs on two EC2 instances in a public subnet with auto-assigned public IP addresses. Route 53 A records for www.example.com and api.example.com point to those addresses. The instances were stopped during maintenance and then started again, but the DNS names now point to addresses that no longer respond. What is the most likely cause?"},
    147: {"prompt":"A retail startup uses Amazon Cognito for Google and Facebook sign-in to its mobile application. Marketing wants a \"try it now\" mode so new users can browse limited, read-only features without creating an account. Backend access must follow least privilege, a second application should not be required, and guests should be able to upgrade to a full account when they later sign in. Which approach meets these requirements?"},
    154: {"prompt":"A company is migrating a production MySQL database from an on-premises data center to Amazon RDS using AWS Database Migration Service (AWS DMS). A separate platform team will create replication instances, define endpoints, and run migration tasks. Security leadership asks which AWS mechanism controls who may create, modify, or delete these DMS resources through the console, CLI, or API. Which mechanism should the architect choose?"},
    163: {"options.3":"Copy the data to Amazon RDS. Use RDS as a data source for Amazon QuickSight and create the dashboards."},
    164: {"prompt":"A company runs a web application in an EC2 Auto Scaling group. The operations team must collect custom, application-level metrics from every instance and visualize them aggregated at the Auto Scaling group level, while retaining the ability to inspect individual instances. Which CloudWatch agent configuration supports this requirement?"},
    196: {"prompt":"An IoT application sends data to Kinesis Data Streams using the default retention settings. A batch job exports stream records to S3 every two days. Some older records are missing when the export runs. What explains the missing data?"},
    198: {"options.0":"An ephemeral backup key (EBK) encrypts the data, and a persistent backup key (PBK) encrypts the EBK before the backup is stored in an S3 bucket in the same Region as the CloudHSM cluster.","options.2":"An ephemeral backup key (EBK) encrypts the data, and a persistent backup key (PBK) encrypts the EBK before the backup is stored in an S3 bucket in a different Region from the CloudHSM cluster."},
    207: {"options.1":"Configure the S3 lifecycle rule to remove unneeded noncurrent object versions after one year."},
    258: {"prompt":"A company creates a VPC with CIDR 10.10.0.0/16, public and private subnets, and an attached internet gateway. The public subnet's route table has a 0.0.0.0/0 route to the gateway. A Linux EC2 instance is launched there with auto-assigned public IPv4 addressing enabled. An administrator cannot connect to it using SSH on port 22. Which of the following is the most likely cause?","options.2":"The instance was not assigned a public IP address."},
    259: {"prompt":"A company needs a 150 GiB data volume for an EC2 instance. Data is accessed infrequently, with occasional throughput spikes during morning and evening processing windows. Cost optimization is a high priority. Which offered EBS volume type is the most cost-effective fit?","options.0":"Provisioned IOPS SSD (io1/io2)."},
    264: {"prompt":"A company runs a two-tier application. Its web tier uses EC2 instances in a public subnet, and its Amazon RDS for MySQL database is in a private subnet. Default network ACLs allow inbound and outbound traffic. End users must reach the web tier only through HTTPS on TCP port 443, and the database must accept connections only from the web tier. Other applications share these subnets and must not be affected. Which two actions meet these requirements?"},
    270: {"prompt":"An application lets users upload and view product images stored in S3. The images must be immediately accessible when requested, and storage costs should automatically adjust as access frequency changes. The company wants to avoid building a custom tiering process. Which storage class best fits?"},
    295: {"options.3":"Use curl to query user data at http://169.254.169.254/latest/user-data/."},
    328: {"prompt":"An ingestion service writes many items to a DynamoDB table in Region A. Every two hours, a secondary application must fetch only the new or changed items and run downstream enrichment and notifications. The design must avoid full-table scans, preserve change ordering, and reliably deliver changes since the previous run. Which solution should the team implement?"},
    338: {"options.0":"Replicate the complete application architecture in another AWS Region and use weight-based routing to distribute traffic.", "options.1":"Replicate the on-premises data center to another location and direct users there during an outage."},
    345: {"prompt":"An application stores product images in S3. It needs immediate access when objects are requested and automatic storage-cost optimization when access declines. The team does not want to build its own tiering workflow. Which S3 storage class should it use?"},
    351: {"prompt":"A securities application uses API Gateway and Lambda with an Aurora database. API caching is enabled on GET /securities to reduce database load and latency. Equity and fixed-income requests must have separate cache entries so that updates to one category do not invalidate the other's entries. The team wants to avoid duplicate stages or APIs. How should it split the cache entries?"},
    565: {"options.2":"Transform the JSON data into Apache Parquet format. Ensure that the user has the lakeformation:GetDataAccess IAM permission required by the data-access workflow."},
    620: {"options.2":"Create an alias record of type AAAA.","options.3":"Create a non-alias record of type A."},
    738: {"prompt":"A serverless application uses AWS Amplify, Amazon API Gateway, and Lambda. The Lambda function connects to an Amazon RDS for MySQL database in a private subnet and also has a dedicated HTTPS function URL. During peak traffic, the database reports \"too many connections\" and users cannot access the application. Which solution addresses this problem?"},
    847: {"prompt":"A company runs Windows-based EC2 instances with IPv4 addresses in private subnets. Installed software must download updates from the internet, but external systems must not be able to initiate connections to the instances. Which service is the most suitable managed component for a highly available outbound-access solution?"},
    879: {"prompt":"An e-commerce application runs on EC2 instances in an Auto Scaling group and uses Amazon RDS for MySQL. The database has slow queries, frequent \"too many connections\" errors, and many open but idle connections. Which solution most directly addresses the connection-management problem cost-effectively?"},
    885: {"prompt":"A restaurant application uses Lambda and SNS to coordinate order processing. Restaurants accept or reject orders, and several functions run in sequence. The team wants a visual workflow, visibility into each step, and managed state transitions and failure handling. Which service should it use?"},
    898: {"prompt":"A team uses CloudFormation to define a gaming platform in three stacks: a Security Stack for security groups, a Network Stack for the VPC and subnets, and an Application Stack for compute resources. Other stacks must reference the security-group ID from the Security Stack. Which CloudFormation feature supports these cross-stack references?"},
    902: {"prompt":"A pharmaceutical company ingests sensitive scientific data in multiple formats. It wants a secure, scalable, central data lake. A cleansing workflow must remove duplicates and anomalies before the data is stored in the lake. Access must be controlled at the row, column, and cell levels for authorized analysts. Which service best supports these data-lake requirements?"},
    964: {"prompt":"A VPC in us-east-1 has an S3 gateway endpoint associated with the main route table used by a public subnet. An EC2 instance in that subnet times out when accessing an S3 bucket in the same Region. Which two configuration problems could cause this network timeout?"},
    966: {"prompt":"A VPC has a primary CIDR block of 10.10.0.0/24. Eight /27 subnets consume that address range, and their available addresses are exhausted. A new application needs 20 EC2 instances that can communicate internally; internet access is not required. What is the most appropriate way to add address capacity to the existing VPC?"},
    967: {"prompt":"VPC A has CIDR 10.10.0.0/16 and subnet 10.10.1.0/24. VPC B has CIDR 10.11.0.0/16 and subnet 10.11.1.0/28. The VPCs have an established peering connection. The team wants routing through that connection to cover only these two subnets, rather than the full VPC ranges. Which route-table configuration should it use?"},
    973: {"prompt":"An existing EFS filesystem has mount targets in VPC A in us-east-1. A new application environment in a separate VPC B in the same Region must access that existing filesystem. How can the company provide access while minimizing resource duplication?"},
    977: {"prompt":"A web application runs on five load-balanced EC2 instances and shares no more than 25 GB of content through EFS. Frequent access creates high throughput demand relative to the small stored dataset. Which offered EFS throughput configuration lets the team provision throughput independently of stored size?"},
    994: {"prompt":"An operations team runs EC2 applications in two custom VPCs, one in US East (Ohio) and the other in US East (N. Virginia). The instances must exchange data without traversing the public internet. Which two steps provide the required private connectivity?"},
}

# Precise, contextual sentence repairs. These run before the general prose rules.
REPLACEMENTS = {
    4:{"prompt":[("AWS The","AWS. The"),("management Which","management. Which")]},
    5:{"prompt":[("compliance However","compliance. However")]},
    14:{"prompt":[("cloud The","cloud. The")]},
    17:{"prompt":[("audience Which","audience. Which")]},
    21:{"prompt":[("replicae During","replicas. During")]},
    33:{"prompt":[("subnete One","subnets. One")]},
    41:{"prompt":[("service Who","service. Who")]},
    50:{"prompt":[("SIO/hour","$10/hour")]},
    56:{"takeaway":[("data/services so","data/services, so")]},
    78:{"options.2":[("lox,'hcost","low-cost")]},
    84:{"explanations.2":[("violate least privilege","violate the principle of least privilege")]},
    92:{"explanations.0":[("choices so","choices, so")]},
    99:{"options.3":[("enforce least privilege","enforce the principle of least privilege")]},
    109:{"takeaway":[("toggled to encrypted","encrypted by toggling a setting")]},
    113:{"explanations.3":[("notifications but","notifications, but")]},
    117:{"prompt":[("(PID","(PII)")]},
    119:{"note":[("origin so users","origin so that users")]},
    134:{"options.1":[("accounts so","accounts, so")]},
    135:{"prompt":[("credentials so","credentials so that")],"options.0":[("usefs identity provider account","user's identity-provider account")]},
    139:{"takeaway":[("Regions so","Regions, so")]},
    140:{"options.2":[("invitation so","invitation so that")]},
    149:{"explanations.2":[("activity so","activity, so")]},
    153:{"prompt":[("tracking so","tracking so that")]},
    180:{"prompt":[("AWS so jobs","AWS so that jobs")]},
    192:{"options.1":[('event"','event')]},
    197:{"note":[("Consider least privilege","Consider the principle of least privilege")]},
    206:{"explanations.1":[("versions but","versions, but")]},
    207:{"options.2":[("one year old objects","objects that are one year old")]},
    216:{"prompt":[("role so the runtime","role so that the runtime")]},
    217:{"options.3":[("use a third-party tool","Use a third-party tool")]},
    220:{"prompt":[("upload so the browser","upload so that the browser")]},
    223:{"prompt":[("us-east-Ice","us-east-1c")]},
    226:{"options.1":[("promot-","promote")],"options.3":[("Snitch","Switch")]},
    240:{"prompt":[("upon investigation","Upon investigation")]},
    246:{"options.0":[("changed and SSH","changed, and SSH")],"options.3":[("stopped-only terminated","stopped; they can only be terminated")]},
    247:{"options.3":[('(EN)"','(EN)')]},
    256:{"options.3":[("upload files directly","Upload files directly")]},
    257:{"prompt":[("worldwide and some","worldwide, and some")]},
    260:{"options.0":[("use all","Use all")],"options.3":[("use mixed","Use a mixed")],"explanations.2":[("All Spot can be interrupted","An all-Spot fleet can be interrupted")]},
    261:{"prompt":[("third- party operations team","A third-party operations team")]},
    275:{"options.3":[('split" the bills','split the bills')]},
    277:{"prompt":[("with least operational overhead","with the least operational overhead")]},
    288:{"prompt":[("enforce least privilege access","enforce least-privilege access")]},
    289:{"prompt":[("users must authenticate","Users must authenticate")]},
    296:{"explanations.2":[("attribute so stack","attribute so that stack")]},
    322:{"options.1":[("orters","objects")]},
    354:{"options.1":[('enable" the new one','enable the new one')]},
    369:{"prompt":[("account but the access","account, but the access")]},
    372:{"prompt":[("suggested to store","suggested storing")]},
    391:{"options.1":[("an Nginx server","an nginx server")]},
    406:{"note":[("is awkward but","is awkward, but")]},
    409:{"explanations.0":[("Budgets tracks","AWS Budgets tracks")]},
    414:{"prompt":[("online stocks trading","online stock-trading"),("at anytime","at any time"),("any time and you","any time, and you")]},
    419:{"prompt":[(".com,i-love", ".com, i-love"),(".com i- love", ".com, i-love")]},
    425:{"prompt":[("issue and how","issue, and how")]},
    429:{"options.1":[("stream'", "stream")]},
    452:{"note":[("key/user name","key/username")]},
    456:{"prompt":[("Intelligence(Al)","intelligence (AI)")]},
    510:{"explanations.0":[("instances so no","instances so that no")]},
    520:{"options.2":[("policy to IAM group","policy to the IAM group")],"explanations.0":[("violates least privilege","violates the principle of least privilege")]},
    527:{"note":[("exceptions so users","exceptions so that users")]},
    532:{"explanations.2":[("transcript text and it","transcript text, and it")]},
    544:{"takeaway":[("uploads so the bucket","uploads so that the bucket")]},
    546:{"explanations.2":[("profile so the SDK","profile so that the SDK")]},
    556:{"prompt":[("globe and it","globe, and it"),("10 MB but","10 MB, but"),("deleted so the total","deleted so that the total")]},
    566:{"prompt":[("bucket but this","bucket, but this")]},
    569:{"prompt":[("brand new IAM user","brand-new IAM user")]},
    578:{"options.1":[("pool and it","pool, and it")]},
    588:{"prompt":[("The studio are","The studio is")]},
    604:{"prompt":[("fault tolerant system","fault-tolerant system")]},
    606:{"explanations.0":[("ephemeral and its","ephemeral, and its")]},
    609:{"explanations.0":[("symptom but a dashboard","symptom, but a dashboard")]},
    613:{"explanations.2":[("can help cleansing","can help cleanse data")]},
    620:{"prompt":[("go Live but","go live, but")]},
    624:{"note":[("enabled and the app","enabled and that the app")]},
    626:{"prompt":[("has both on-premises data center as well as AWS cloud infrastructure","has both an on-premises data center and AWS cloud infrastructure")]},
    629:{"options.2":[("'Grant\"",'"Grant"')]},
    632:{"note":[("ASG so unhealthy","ASG so that unhealthy")]},
    633:{"explanations.3":[("A worker-count change changes compute","Changing the worker count changes compute capacity")]},
    639:{"note":[("Delivery is best effort","Delivery is on a best-effort basis")]},
    640:{"note":[("preserve least privilege","preserve the principle of least privilege")]},
    648:{"prompt":[("market and it","market, and it")]},
    673:{"takeaway":[("uploads so the bucket","uploads so that the bucket")]},
    686:{"prompt":[("brand new IAM user","brand-new IAM user")]},
    688:{"takeaway":[("metric so target","metric so that target")]},
    690:{"prompt":[("using AWS Organizations","Using AWS Organizations")]},
    709:{"note":[("is awkward but","is awkward, but")]},
    843:{"prompt":[("upon checking","Upon checking")]},
    883:{"explanations.0":[("work so workers","work, so workers")]},
    884:{"prompt":[("cause and how","cause, and how")],"options.1":[("renewed,request","renewed; request")],"options.3":[("expired,contact","expired; contact")]},
    888:{"prompt":[("exists but required","exists, but required")]},
    899:{"explanations.2":[("execution so workers","execution, so workers")]},
    900:{"explanations.0":[("access but its","access, but its")],"explanations.1":[("access but Glacier","access, but Glacier")]},
    904:{"prompt":[("lovv'-cost","low-cost")],"explanations.1":[("tradeoff but its","tradeoff, but its")]},
    933:{"explanations.0":[("workloads but ordinary","workloads, but ordinary")]},
    935:{"prompt":[("retained so the data","retained so that the data")]},
    948:{"explanations.2":[("idempotent so a repeated","idempotent so that a repeated")]},
    979:{"options.0":[('sent."','sent.')]},
    988:{"prompt":[("both mission-critical data as well as non-essential batch jobs","both mission-critical data and non-essential batch jobs")]},
    1023:{"prompt":[("recur, so staff","recur so that staff")]},
}
for number, fields in {
    147:{"prompt":[("follow least privilege","follow the principle of least privilege")]},
    163:{"prompt":[("bucket Leadership","bucket. Leadership")]},
    170:{"prompt":[("eg- security","e.g., security"),("eg-security","e.g., security")]},
    172:{"prompt":[("internet In the future","internet. In the future")]},
    188:{"options.2":[("TTL - O","TTL to 0")]},
    271:{"prompt":[("latenc r sensitive","latency-sensitive"),("latency r sensitive","latency-sensitive")]},
    311:{"prompt":[("under- utilization","underutilization")],"options.2":[("capac ty","capacity")]},
    326:{"prompt":[("After scaling out your group","After scaling out, your group")]},
    349:{"prompt":[("source 'P","source IP")]},
    997:{"prompt":[("a vpc","a VPC"),("on-Demand","On-Demand")]},
    220:{"prompt":[("bucket Security requires","bucket. Security requires")]},
    251:{"prompt":[("Region During a compliance","Region. During a compliance")]},
    262:{"prompt":[("CloudFormation To detect","CloudFormation. To detect")]},
    323:{"prompt":[("CloudFront Security requires","CloudFront. Security requires")]},
    346:{"prompt":[("bucket After 60 days","bucket. After 60 days")]},
}.items():
    for field, replacements in fields.items():
        REPLACEMENTS.setdefault(number,{}).setdefault(field,[]).extend(replacements)

PROTECTED = re.compile(r"\.NET\b|CloudWatch Logs|Flow Logs|Logs Insights|Local Zones?|Load Balancers?|https?://\S+|arn:[^\s,;]+|`[^`]+`|\b(?:[a-z]+:)?[A-Za-z]+(?:[A-Z][a-z0-9]+){2,}\b|\b[a-z]+\d[a-z0-9]*\.(?:nano|micro|small|medium|large|xlarge|\d+xlarge)\b|\b[a-z0-9_-]+(?:\.[a-z0-9_-]+)*\.(?:com|org|net|aws|io|internal)\b")
CAPITALS = {"Large","Less","Latest","Low","Lower","Lowest","Long","Little","Live","Local","Located","Locally","Level","Levels","Life","Like","Logs","Log","Line","Limit","Limitations","Load","Loads","Launch","Launching","Launched"}

def lexical(value):
    for before, after in sorted(PHRASES.items(),key=lambda p:-len(p[0])):
        value = value.replace(before,after)
    # The apostrophe/quote fragments here are OCR damage, not English quotations.
    value = re.sub(r"['\"]{1,2}thout\b", "without", value)
    for before, after in WORDS.items():
        value = re.sub(r"(?<![A-Za-z0-9_])"+re.escape(before)+r"(?![A-Za-z0-9_])",lambda _:after,value)
    for before, after in AMERICAN.items():
        value = re.sub(r"\b"+before+r"\b",lambda m: after.capitalize() if m[0][0].isupper() else after,value,flags=re.I)
    return value

def clean(value, field):
    value = lexical(value)
    value = re.sub(r"\b(?:us|eu|ap|ca|sa|af|me|il|mx)-\s*(?:east|west|central|south|north|northeast|southeast)-\s*[lI](?:[a-z])?\b",lambda m: re.sub(r"[lI](?=[a-z]?$)","1",re.sub(r"\s+","",m[0])),value)
    value = re.sub(r"\bus-vvest-", "us-west-",value)
    value = re.sub(r"\bVPC-[Il]\b", "VPC-1",value)
    value = re.sub(r"\bon-prem\b(?!ises)", "on-premises",value)
    value = re.sub(r"\bsolutions? [Aa]rchitect\b", "solutions architect",value,flags=re.I)
    value = re.sub(r"\bavailability zones?\b",lambda m: "Availability Zones" if m[0].lower().endswith("s") else "Availability Zone",value,flags=re.I)
    # Protect URLs, ARNs, dotted instance types, and technical expressions before punctuation.
    protected = []
    def hold(m):
        protected.append(m[0]); return f"\uE000{len(protected)-1}\uE001"
    value = PROTECTED.sub(hold,value)
    value = re.sub(r"(?<=[A-Za-z])-\s+(?=[A-Za-z])","-",value)
    value = re.sub(r"(?<=[A-Za-z])\s+-(?=[A-Za-z])","-",value)
    value = re.sub(r"\bbi-directional\b","bidirectional",value,flags=re.I)
    value = re.sub(r"\bhighly-(available|scalable)\b",r"highly \1",value,flags=re.I)
    value = re.sub(r"\s+([,;!?])",r"\1",value)
    value = re.sub(r"\s+\)",")",value)
    value = re.sub(r"([,;!?])(?=[A-Za-z])",r"\1 ",value)
    value = re.sub(r"(?<=[a-z])\.(?=[A-Z])",". ",value)
    value = re.sub(r"(?<=[A-Za-z0-9)])\s+(?=(?:The|However|They|This|These|Their|It|There|You)\b)",lambda m: " " if re.search(r"\b(?:and|or|to|of|for|with|in|on|that|than|whether|because|if)$",value[:m.start()],re.I) else ". ",value)
    value = re.sub(r"\s+\.",".",value)
    value = re.sub(r"\b([A-Za-z]+)\b",lambda m: m[0].lower() if m[0] in CAPITALS and m.start()>0 and not re.search(r"[.!?:]\s*$",value[:m.start()]) else m[0],value)
    for i, token in enumerate(protected): value=value.replace(f"\uE000{i}\uE001",token)
    # Some OCR splits only become recognizable after spaces/hyphens are repaired.
    value = lexical(value)
    value = re.sub(r"\s+"," ",value).strip()
    value = re.sub(r"\bon-prem\b(?!ises)", "on-premises",value)
    if not field.startswith("options."):
        value = re.sub(r"^(cfn-[a-z-]+)\s+",r"The \1 helper script ",value)
        value = re.sub(r"^(aws:[A-Za-z]+)\s+",r"The \1 condition key ",value)
        value = re.sub(r"^awsvpc\s+","The awsvpc network mode ",value)
        value = re.sub(r"^append-config\s+","The append-config action ",value)
        value = re.sub(r"^aggregation_dimensions\s+","The aggregation_dimensions setting ",value)
        value = re.sub(r"^lakeformation:GetDataAccess\s+","The lakeformation:GetDataAccess permission ",value)
    if value and value[0].islower() and not re.match(r"(?:https?://|arn:|cfn-|aws:|awsvpc|x-amz-|[a-z]+\.[a-z]+|[a-z]+_[a-z]+|max-age|lakeformation:|aggregation_dimensions|append-config)",value):
        value = value[0].upper()+value[1:]
    if field.startswith("options."):
        # Do not append punctuation to standalone code, API identifiers, headers, or URLs.
        code = re.match(r"^(?:arn:|https?://|x-amz-|CREATE |SELECT |GRANT |ALTER |DELETE |INSERT |\{|\[)",value) or re.fullmatch(r"[A-Za-z0-9_:/.$*-]+",value)
        if value and not code and value[-1] not in ".?!;:}": value+="."
    elif field != "title" and value and value[-1] not in ".?!:}":
        value+="."
    return value

def prompt_layout(value, select):
    value = re.sub(r"\s*\((?:select|choose)\s+(?:one|two|three|four|[1-4])(?:\s+answers?)?\.?\)\.?\s*$","",value,flags=re.I).strip()
    # Preserve question qualifiers and negation. Separate the final question from its scenario.
    matches = list(re.finditer(r"\b(?:Which|What|How|Who|Where|Why)\b",value))
    if matches:
        at=matches[-1].start()
        if at>35:
            scenario=value[:at].rstrip(" -")
            if scenario[-1] not in ".?!:": scenario+="."
            value=scenario+"\n\n"+value[at:]
        if value.endswith(".") and "?" not in value[value.rfind("\n\n")+2:]: value=value[:-1]+"?"
    elif not value.endswith("?"):
        value=value.rstrip(".")+".\n\nWhich solution best meets these requirements?"
    if select>1:
        value+=f" (Select {['ZERO','ONE','TWO','THREE','FOUR'][select]}.)"
    return value

def apply_copyedits(bank):
    ledger={}
    # Some earlier editorial variants share list objects. Copy before changing prose.
    for q in bank:
        q["options"] = list(q["options"])
        q["explanations"] = list(q["explanations"])
        if q.get("reasoning"): q["reasoning"] = dict(q["reasoning"])
    before_contract=[[q["id"],len(q["options"]),q["select"],q["correct"],q["status"]] for q in bank]
    for q in bank:
        if q["status"]!="ready": continue
        changes={}
        fields={"prompt":q["prompt"],"takeaway":q["takeaway"],"note":q["note"]}
        fields.update({f"options.{i}":v for i,v in enumerate(q["options"])})
        fields.update({f"explanations.{i}":v for i,v in enumerate(q["explanations"])})
        if q.get("reasoning"):
            fields.update({f"reasoning.{k}":v for k,v in q["reasoning"].items() if isinstance(v,str)})
        for field,before in fields.items():
            value=FIELDS.get(q["number"],{}).get(field,before)
            for old,new in REPLACEMENTS.get(q["number"],{}).get(field,[]): value=value.replace(old,new)
            value=clean(value,field) if value else value
            if field=="prompt": value=prompt_layout(value,q["select"])
            check=clean(value,field) if value else value
            if field=="prompt":check=prompt_layout(check,q["select"])
            assert value==check, f"Non-idempotent copy rule: #{q['number']} {field}: {value!r} -> {check!r}"
            if value==before:continue
            changes[field]={"before":before,"after":value}
            if field.startswith(("options.","explanations.")):
                name,index=field.split(".");q[name][int(index)]=value
            elif field.startswith("reasoning."):q["reasoning"][field.split(".")[1]]=value
            else:q[field]=value
        title=clean(q["title"],"title")
        if title!=q["title"]:changes["title"]={"before":q["title"],"after":title};q["title"]=title
        if changes:ledger[q["id"]]={"number":q["number"],"fields":changes}
    after_contract=[[q["id"],len(q["options"]),q["select"],q["correct"],q["status"]] for q in bank]
    assert before_contract==after_contract,"Copy editing changed a scoring contract"
    digest=hashlib.sha256(json.dumps(before_contract,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
    report={"reviewedAt":REVIEWED_AT,"reviewedRecords":sum(q["status"]=="ready" for q in bank),"editedRecords":len(ledger),"editedFields":sum(len(r["fields"]) for r in ledger.values()),"scoringContractSha256":digest,"edits":ledger}
    (ROOT/"data/copy-edit-review.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("Copy edit:",{k:v for k,v in report.items() if k!="edits"})
    return report
