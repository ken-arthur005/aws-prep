"""Closed editorial decisions for the supplied HTML collection.

The supplied key is never copied into a scored question. Matches below were reviewed
against the complete bank/raw variants; new records have independently written text.
"""
REVIEWS = {}
HOLDS = {}

MATCHES = {int(a):int(b) for token in """
7:643 8:356 24:651 29:685 34:460 35:527 36:461 37:462 38:463 39:684 40:722
42:675 43:681 71:417 72:418 73:419 74:420 75:421 76:422 77:423 78:424 79:425
80:426 81:427 82:428 83:429 84:430 85:431 86:432 87:433 88:434 89:435 90:436
91:437 92:438 94:440 96:442 97:443 98:509 99:510 100:444 101:445 102:446
103:447 104:448 105:449 106:516 107:450 108:451 109:452 110:454 111:520 112:455
113:456 114:523 115:457 116:458 117:459 118:608 119:381 120:569 121:687 122:688
123:689 125:564 126:692 127:604 128:616 129:607 130:706 131:707 132:406 133:552
135:367 136:597 137:363 138:364 140:724 141:360 142:407 143:408 144:409 145:410
146:412 148:414 149:415 150:416 151:627 154:628 155:629 156:630 158:631 159:632
160:633 161:634 162:635 163:636 164:637 166:639 167:640 170:641 171:642 172:644
173:646 175:650 176:540 177:653 178:655 179:656 181:658 182:659 183:663 184:664
185:665 186:667 187:668 188:568 189:543 190:671 191:612 192:544 193:674 194:854
195:855 197:583 198:584 199:585 201:588 202:589 203:591 205:593 206:594 207:595
208:596 210:599 211:600 212:601 213:602 214:605 215:606 216:609 217:610 218:611
219:613 220:614 221:615 222:618 223:619 224:620 226:622 227:623 229:624 230:625
231:626 232:545 233:546 234:547 235:548 236:549 237:551 238:553 239:554 240:556
241:557 242:559 244:561 245:566 246:570 247:571 248:572 249:573 250:574 252:577
253:579 254:839 255:580 256:581 257:582 258:843 259:846 260:847 261:848 262:849
263:850 264:851 265:852 266:853 267:979 268:981 269:982 270:983 272:987 273:988
275:993 276:1003 277:1021 278:1033 279:1034 280:1040 281:532 282:533 283:534
284:535 285:798 286:537 287:539 288:541 289:542 290:382 291:383 293:384 295:386
296:387 297:388 298:774 299:393 300:399 302:357 303:730 304:359 306:738 307:741
308:744 309:745 310:746 311:365 312:368 313:369 314:370 315:371 316:372 317:373
318:376 319:377 320:378 321:379 322:380
2:661 31:52 54:125 56:555 66:619 70:954 93:439 95:441 124:690 139:723 147:413
152:345 165:638 174:648 200:586 204:592 209:598 225:621 243:820 251:575 271:986
274:991 292:767 294:385 305:737
""".split() for a,b in [token.split(":")]}
# Same requirement/decision, with different distractors; one native item represents each family.
MATCHES.update({30:"html-010",47:"html-023"})

# Existing ambiguities exposed by the independent conflict review. Keep old grading
# records for history, but stop sampling these statements for new scored sessions.
STUDY_EXCLUSIONS = {
    541:"The choices conflate On-Demand instances with explicit capacity reservations and imply a built-in recurring reservation schedule. No single complete, unqualified architecture is specified. Historical results are retained; practise the capacity-versus-discount distinction in the revision guide instead.",
    554:"Both ECS and Docker on Elastic Beanstalk can meet parts of this broad migration description. The source does not distinguish direct container orchestration from a managed application environment, so its single-answer key is not uniquely supported.",
    626:"The choose-two source mixes lifecycle transition timing, storage-duration charging, and archival retrieval assumptions. It does not provide a uniquely current set of two valid designs with the necessary cost/retrieval constraints. Historical answer selections are preserved rather than silently regraded.",
    981:"HPA can be paired with either a correctly configured Cluster Autoscaler or Karpenter. The vague failed/rescheduled-pod wording does not reliably eliminate Karpenter, so selecting exactly two cannot establish a unique complete pair.",
}

PRIMARY = {
 "streams":("DynamoDB Streams and Lambda","https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.html"),
 "lambda":("Lambda execution and scaling","https://docs.aws.amazon.com/lambda/latest/dg/welcome.html"),
 "iam":("SAML federation and IAM roles","https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html"),
 "waf":("WAF rate-based rules","https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html"),
 "s3":("S3 storage classes","https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html"),
 "accel":("S3 Transfer Acceleration","https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html"),
 "version":("S3 Versioning and MFA Delete","https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html"),
 "monitor":("RDS Enhanced Monitoring","https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html"),
 "gateway":("S3 File Gateway","https://docs.aws.amazon.com/filegateway/latest/files3/what-is-file-s3.html"),
 "as":("EC2 Auto Scaling termination policies","https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html"),
 "efs":("Amazon EFS","https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html"),
 "firewall":("AWS Network Firewall","https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html"),
 "ipv6":("Egress-only internet gateways","https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html"),
 "rds":("RDS Multi-AZ deployments","https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html"),
 "dms":("Database Migration Service","https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html"),
 "events":("EventBridge ECS targets","https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html"),
 "aurora":("Aurora endpoints","https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html"),
 "api":("API Gateway throttling","https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html"),
 "canary":("API Gateway canary releases","https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.html"),
 "env":("Lambda environment-variable encryption","https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars-encryption.html"),
 "ontap":("FSx for NetApp ONTAP","https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html"),
 "lustre":("FSx for Lustre","https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html"),
 "windows":("FSx for Windows File Server","https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html"),
 "url":("S3 presigned URLs","https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html"),
 "cw":("CloudWatch agent host metrics","https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html"),
 "macie":("Macie sensitive-data discovery","https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html"),
 "client":("S3 client-side encryption","https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingClientSideEncryption.html"),
 "artifact":("AWS Artifact reports","https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html"),
 "dynamo":("DynamoDB data model","https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html"),
 "keys":("KMS CloudHSM key stores","https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html"),
 "tracking":("Target tracking scaling","https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html"),
 "invoke":("Aurora MySQL Lambda integration","https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Lambda.html"),
 "replicas":("Aurora replica auto scaling","https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html"),
 "global":("Aurora Global Database","https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html"),
 "lock":("S3 Object Lock","https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html"),
 "access":("S3 VPC-only access points","https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-vpc.html"),
 "shield":("AWS Shield protections","https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html"),
 "ram":("Sharing resources with RAM","https://docs.aws.amazon.com/ram/latest/userguide/what-is.html"),
 "auth":("IAM database authentication","https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html"),
 "beanstalk":("Elastic Beanstalk environments","https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html"),
 "lake":("Lake Formation cross-account access","https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-permissions.html"),
 "transfer":("Transfer Family","https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html"),
 "notifications":("S3 event destinations","https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-event-types-and-destinations.html"),
 "glue":("Glue job triggers","https://docs.aws.amazon.com/glue/latest/dg/trigger-job.html"),
 "endpoints":("S3 gateway endpoints","https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html"),
 "manager":("Firewall Manager policies","https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html"),
 "kinesis":("Lambda stream processing","https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html"),
 "secrets":("ECS secrets from Parameter Store","https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar-ssm-paramstore.html"),
 "subnets":("VPC subnet design","https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html"),
 "default":("EBS encryption by default","https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html"),
 "edge":("CloudFront geographic restrictions","https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html"),
}

def r(i, answer, domain, topic, refs, prompt, options, takeaway, explanations, note=""):
    assert i not in MATCHES and i not in REVIEWS
    REVIEWS[i]={"correct":[ord(c)-65 for c in answer],"domain":domain,"topic":topic,"refs":refs.split(),"prompt":prompt,"options":options.split("|"),"takeaway":takeaway,"explanations":explanations.split("|"),"note":note}
    assert len(REVIEWS[i]["options"])==len(REVIEWS[i]["explanations"]),i

def h(i, reason):
    assert i not in MATCHES and i not in REVIEWS
    HOLDS[i]=reason

r(1,"C","secure","Data protection before storage","kinesis dynamo",
 "A healthcare analytics pipeline receives real-time records containing personally identifiable information (PII). Records must be anonymized before reaching the destination NoSQL database, and raw PII must not be staged in an S3 data lake. Which design meets these requirements?",
 "Write raw records to DynamoDB and anonymize them later using DynamoDB Streams.|Transform records with Data Firehose and deliver them to Amazon Redshift.|Ingest records with Kinesis Data Streams, anonymize them with Lambda, and write the results to DynamoDB.|Write raw records to an S3 data lake and use an S3-triggered Lambda function to anonymize them before writing to DynamoDB.",
 "Place the transformation before the protected destination; reacting after a database write is too late.",
 "The unmasked record reaches the database before the change stream triggers anonymization.|Redshift is a warehouse, not the required NoSQL destination.|Lambda transforms the stream records before writing the anonymized results to DynamoDB.|This stages raw PII in S3, violating the explicitly stated intermediate-storage restriction.",
 "Study variant: the S3 staging restriction is explicit because the supplied wording only prohibited raw PII in the NoSQL database. Configure stream retention, access, encryption, and idempotent processing separately.")
r(3,"C","performance","Bursty serverless APIs","lambda api",
 "A startup has an RDS-backed application with low activity between sudden product-announcement traffic bursts. It wants an API compute layer that can scale quickly without maintaining an idle server fleet. Which offered design is the best fit?",
 "API Gateway with an EC2-backed ECS service.|API Gateway with an Elastic Beanstalk EC2 environment.|API Gateway with Lambda functions.|API Gateway with an EC2 Auto Scaling group.",
 "Lambda fits bounded event-driven API work; protect the database from the resulting concurrency.",
 "EC2-backed containers need instance capacity and scaling configuration, even when service scaling is enabled.|Beanstalk manages an application environment but still operates a provisioned EC2 fleet.|Lambda supplies request-driven compute without the application managing a standing instance fleet.|An EC2 group needs instance launch/readiness time and capacity planning for the burst.",
 "Lambda has quotas and scaling limits; it does not guarantee arbitrary instantaneous capacity. RDS remains chargeable when idle, and connection pooling or concurrency controls may be needed.")
r(4,"D","resilient","Database change notifications","streams",
 "A social application stores user activity in DynamoDB. It must react to item changes and email the relevant followers with minimal custom polling infrastructure. Which integration should it use?",
 "Run a custom Kinesis adapter inside Lambda to poll the DynamoDB Streams endpoint manually.|Maintain a KCL worker application to poll DynamoDB Streams and send SNS messages.|Use DAX as the event source for change notifications.|Enable DynamoDB Streams and a Lambda event source mapping; let the function identify followers and publish suitable SNS notifications.",
 "DynamoDB Streams is a change feed; DAX is a read cache.",
 "Lambda already provides a managed event source mapping, so a custom polling adapter adds unnecessary work.|A custom KCL worker can consume compatible streams but adds worker management compared with the native integration.|DAX caches reads and does not replace the DynamoDB item-change stream.|The managed mapping delivers change records to Lambda, where application logic selects recipients and sends notifications.",
 "Configure least-privilege roles, subscription/follower routing, retries, and idempotency. A stream does not automatically determine the application's followers.")
r(5,"AB","secure","Federated per-user access","iam",
 "A company wants 1,200 employees to use existing corporate AD/LDAP identities for SSO to personal document storage in S3. Each employee must be limited to an assigned prefix without creating a separate IAM user for every employee. Which two components are required?",
 "A suitable identity-provider/federation flow that obtains temporary STS credentials.|IAM roles and policies scoped to the user's assigned S3 prefix using trusted identity attributes.|WorkDocs as the mechanism that automatically maps every user to the S3 prefix.|A third-party SSO product without AWS role or S3 permission configuration.|A matching long-lived IAM user for each corporate directory user.",
 "Federation establishes identity; IAM policies enforce the resource scope.",
 "A supported federation flow reuses the corporate identity and obtains temporary AWS access.|Trusted identity/session attributes and least-privilege policies enforce the intended per-user prefix boundary.|WorkDocs is not the permission-mapping mechanism required for arbitrary S3 prefixes and is retired.|An SSO product still needs the AWS role and resource authorizations; the product name alone grants nothing.|Duplicating all users in IAM contradicts the stated federated-access requirement.")
r(6,"B","secure","Rate-based web protection","waf",
 "An ALB-backed website receives sustained excessive HTTP requests from individual clients. Offending addresses change over time, so manually maintaining an IP block list is impractical. Each abusive client exceeds a defined request-rate threshold. Which control best limits this traffic?",
 "Create a regular WAF rule without a request-matching pattern or rate condition.|Create a suitably scoped WAF rate-based rule and associate the web ACL with the ALB.|Maintain subnet NACL deny entries for every observed source address.|Add explicit deny rules to the ALB security group.",
 "Rate-based rules match measured request rates; an IP list alone does not express a rate policy.",
 "A regular rule needs a meaningful match condition and does not implement the requested rate threshold by itself.|The rule can count requests using an appropriate aggregation key and limit sources exceeding its threshold.|A manually maintained list becomes stale as sources change and does not directly implement HTTP request-rate control.|Security groups are allow-only and cannot express a WAF-style HTTP rate rule.",
 "Clarification: each abusive aggregation key exceeds the threshold. Low-rate distributed traffic or rapid address rotation can evade a per-IP limit and needs additional controls.")
r(9,"B","performance","Long-distance uploads","accel",
 "Weather stations in many countries each upload roughly 600 GB of data over high-speed internet links to one S3 bucket in Northern Virginia. Which offered feature is designed to improve long-distance transfers to that central bucket while allowing parallel upload parts?",
 "Use Site-to-Site VPN as the upload acceleration service.|Enable S3 Transfer Acceleration and use multipart uploads.|Upload into separate regional buckets and add cross-Region replication for every source.|Ship an offline Snowball device for each upload.",
 "Transfer Acceleration optimizes the long-distance S3 path; multipart upload parallelizes the object transfer.",
 "VPN supplies encrypted network connectivity, not this managed S3 upload-acceleration feature.|The acceleration endpoint uses edge ingress and multipart upload can transfer parts concurrently.|An extra regional copy and replication pipeline add stages rather than directly optimizing the central upload endpoint.|Device shipment is not the appropriate repeated online transfer path when suitable high-speed connectivity already exists.",
 "Benchmark actual improvement and cost. Transfer Acceleration is not a guarantee of faster transfer for every source or connection.")
r(10,"CD","resilient","Recoverable S3 object changes","version",
 "An S3 application must recover earlier object contents after accidental overwrites or deletes. It also needs an MFA requirement for permanently deleting retained object versions. Which two features provide these specific controls?",
 "Allow access only through presigned URLs.|Deny DeleteObject but allow overwrites and permanent version deletion.|Enable MFA Delete with the required supported configuration.|Enable S3 Versioning.|Use Intelligent-Tiering.",
 "Versioning preserves historical contents; MFA Delete adds protection to permanent version deletion.",
 "A temporary access URL does not preserve an earlier object version or impose the requested MFA deletion check.|This incomplete policy does not cover the stated overwrite and permanent-version-deletion requirements.|MFA Delete adds the supported MFA requirement to protected version-deletion/versioning operations.|Versioning retains earlier versions, allowing recovery after accidental changes.|Tiering controls storage cost and access tiers, not object version retention or MFA checks.",
 "Versioning is recovery protection rather than a blanket ban on writes/deletes. Carefully scope permissions and configure MFA Delete through its supported root-authorized workflow.")
r(11,"B","resilient","Database operating-system visibility","monitor",
 "An RDS-backed application needs OS-level visibility into database process and thread CPU/memory usage. Default database monitoring does not provide the required per-process view. Which option should the team enable?",
 "Inspect only the default CloudWatch CPUUtilization metric.|Enable RDS Enhanced Monitoring with appropriate permissions.|Assume the default RDS console already supplies every process CPU% and MEM% value.|Log into the managed RDS host to install a custom process-monitoring script.",
 "Enhanced Monitoring supplies supported guest OS/process evidence; a single aggregate CPU metric cannot identify the process.",
 "An aggregate CPU metric does not supply the requested process/thread breakdown.|Enhanced Monitoring gathers supported OS-level metrics and process information at the configured interval.|The required process view depends on the appropriate monitoring feature rather than being implied by default metrics.|Ordinary managed RDS does not expose arbitrary host login for installing the proposed script.")
r(12,"D","cost","Hybrid file access and archival","gateway s3",
 "A company needs SMB access from its data center to durable cloud-backed documents, with a local working-set cache. Documents must remain online for six months and can then move to long-term archival storage for another ten years. Which offered design best preserves the file interface with minimal infrastructure management?",
 "Use Direct Connect and EBS volumes, then move their snapshots directly through an S3 object lifecycle rule.|Use Snowmobile as the permanent SMB access service.|Use a Tape Gateway as the SMB document file share.|Use S3 File Gateway for SMB access and a suitable S3 lifecycle/archive policy after the online-access period.",
 "File Gateway provides the ongoing file interface; lifecycle policies govern the supported object's storage lifetime.",
 "A network connection and EBS volumes do not supply this managed SMB/S3-object interface or the claimed lifecycle path.|An offline transport device is not an ongoing SMB share and Snowmobile is obsolete.|Tape Gateway exposes a virtual tape library, not the required ordinary SMB file share.|File Gateway provides SMB access and local caching, while the S3-backed objects can follow the configured supported storage lifecycle.",
 "A cache is not a guarantee that every recent file remains pinned locally. Archived objects require the appropriate restore/access workflow; design retention and recovery separately.")
r(13,"D","resilient","Scale-in selection","as",
 "An EC2 Auto Scaling group spans three AZs and uses the default termination policy. After selecting the AZ to preserve balance during scale-in, it must choose among otherwise eligible instances in that AZ. Which offered configuration characteristic does the default policy prefer to retire?",
 "The instance that has simply been running the longest.|The instance with the fewest application sessions.|An instance chosen randomly before evaluating configuration.|An instance using the oldest applicable launch template/configuration.",
 "Default scale-in first considers AZ balance, then the configured termination-selection priorities.",
 "Instance age alone is not the same as the configuration priority of the default policy.|Application session count is not a standard default termination-policy input.|The policy evaluates its documented priorities rather than starting with an unrestricted random choice.|Retiring an older launch configuration/template is a relevant default priority within the eligible selected-AZ candidates.",
 "Clarification makes the AZ-selection step explicit. Mixed purchasing options, allocation strategy, protection, and other documented tie-breaks can further constrain selection.")
r(14,"A","performance","Shared POSIX storage","efs",
 "A Linux CMS runs across an Auto Scaling fleet and stores uploaded documents on one instance's EBS volume. It needs a scalable, highly available POSIX/NFS shared filesystem accessible to the fleet. Which offered service is the best fit?",
 "Use Regional Amazon EFS with appropriate mount targets and permissions.|Upgrade the existing EBS volume's provisioned IOPS.|Use ElastiCache as the durable shared filesystem.|Use S3 directly as if it were a native POSIX filesystem.",
 "A shared filesystem requirement is different from faster local block storage or an object API.",
 "Regional EFS provides the shared Linux/NFS filesystem and regional resilience pattern requested.|More IOPS does not turn an AZ-scoped block device into an ordinary multi-AZ shared filesystem.|An in-memory cache is not the durable POSIX file service described.|S3 provides object semantics; using its API requires a different application access model.",
 "Study variant repairs the missing EFS choice in an older defective capture and makes the Linux/POSIX access requirement explicit.")
r(15,"C","secure","IPv6 egress and inspection","ipv6 firewall",
 "An EC2 workload must initiate IPv6 connections to the internet while preventing unsolicited inbound IPv6 connections. Its routed traffic also needs a supported inline inspection/filtering layer. Which offered design supplies both capabilities?",
 "Use a public IPv4 NAT gateway and Firewall Manager alone as the packet-inspection engine.|Use a PrivateLink service endpoint and GuardDuty as the internet-egress filter.|Use an egress-only internet gateway and correctly routed Network Firewall endpoints/rules.|Use an ordinary internet gateway and Traffic Mirroring as an inline blocking firewall.",
 "An egress-only gateway controls IPv6 initiation; Network Firewall performs the supported inline inspection.",
  "This confuses IPv4 NAT with the requested native IPv6 path and central policy rollout with inspection.|A service endpoint does not supply general internet egress, and GuardDuty is detection rather than inline blocking.|The gateway supplies the IPv6 outbound-only pattern and routed firewall endpoints provide the inspection control.|An IGW is not inherently outbound-only, and mirroring copies packets rather than blocking them inline.")
r(16,"DE","resilient","Oracle migration and failover","rds dms",
 "An on-premises Oracle application must move to AWS with minimal engine changes and remain available after a database instance failure. Which two actions provide the appropriate managed destination and supported migration mechanism?",
 "Enable RMAN alone as the entire availability and migration design.|Convert the schema to a different engine even though Oracle compatibility is required.|Use a single-instance Aurora cluster as a drop-in Oracle replacement.|Configure a suitable RDS for Oracle Multi-AZ DB instance deployment.|Use a supported DMS migration task and controlled cutover for the Oracle data.",
 "Choose the destination's availability architecture separately from the data migration process.",
 "A backup utility alone does not establish the complete managed migration and standby failover design.|A same-engine migration does not inherently require heterogeneous schema conversion.|Aurora is not Oracle-compatible and a lone compute instance is not the stated managed standby design.|A supported RDS for Oracle Multi-AZ deployment supplies the managed standby/failover architecture.|DMS can migrate supported Oracle data and changes when configured with the required logging and permissions.")
r(17,"D","resilient","Event-driven Fargate jobs","events",
 "Each new object in S3 should start one independent Fargate processing task. The team wants the least custom invocation code and can configure S3 events, EventBridge, and IAM permissions. Which offered design is the most direct?",
 "Use a CloudWatch alarm to edit an ECS service's desired count for each object.|Use EventBridge to call a Lambda function that manually invokes StartTask for Fargate.|Use a metric alarm as an indirect detector of arbitrary CloudTrail traffic.|Use an EventBridge rule with a supported ECS RunTask target and Fargate task/network configuration.",
 "An event can start an independent ECS task without changing a long-running service's desired count.",
 "Changing a service count is not a direct one-job-per-object invocation and requires separate scale-in semantics.|StartTask does not support Fargate; use RunTask. Even a corrected Lambda invoker adds code when the native ECS target fits.|An aggregate metric alarm is an indirect and incomplete substitute for matching the object-created event.|The supported target can start a standalone Fargate task directly with the configured invocation role.",
 "Study variant distinguishes standalone RunTask jobs from scaling an ECS service. Configure retries, duplicate-event handling, and network access; one object event is not an exactly-once execution guarantee.")
r(18,"A","performance","Aurora workload endpoints","aurora",
 "An Aurora cluster has high-capacity and low-capacity reader instances. Read-only production queries should use only the high-capacity readers, while internal reporting should use only the low-capacity readers. Writes already use the writer endpoint. Which approach gives the required workload separation?",
 "Create separate suitable Aurora custom reader endpoints for the two instance subsets and route each read workload accordingly.|Send production reads to one instance endpoint and all reports to the writer endpoint.|Assume Aurora automatically classifies queries and chooses a reader by business purpose.|Send both workloads to the general reader endpoint without separating its members.",
 "Custom reader endpoints can expose chosen reader subsets; an endpoint cannot infer business intent from every query.",
 "Separate custom endpoints and application routing express the two desired reader groups.|This does not distribute production reads across the intended group and sends reporting load to the writer.|Aurora does not automatically infer the stated workload classification and endpoint policy.|The general reader endpoint does not enforce this explicit high/low reader-subset separation.",
 "Clarification limits the split workloads to reads. Custom reader endpoints do not replace the writer endpoint for write operations.")
r(19,"D","resilient","Gradual API releases","canary",
 "A Regional API Gateway REST API uses a custom domain. A new deployment should receive a small percentage of traffic first, be monitored, and then be gradually promoted while preserving the customer-facing domain. Which offered release mechanism is the most direct fit?",
 "Create a replacement API and immediately point all traffic to it without validation.|Overwrite the production API definition and immediately send all traffic to it.|Build two complete separate environments even though the native staged-release feature is sufficient.|Configure a canary deployment on the API stage, monitor it, and progressively increase the canary traffic percentage.",
 "A canary release limits initial exposure; it is not a guarantee of database-level rollback or zero data loss.",
 "Immediate cutover exposes all customers to an unvalidated deployment.|An immediate overwrite does not supply the requested percentage-based validation period.|Blue/green can be valid, but adds an extra environment when the specified native canary mechanism fits.|A supported stage canary directly supplies controlled traffic percentages and gradual promotion.",
 "Use compatible backend/data changes, health monitoring, and rollback procedures. A canary deployment is configured on a stage, not an automatically isolated new database environment.")
r(20,"C","secure","Lambda configuration secrecy","env",
 "A Lambda function stores database and API credentials in environment variables. Configuration viewers who lack KMS decrypt permission must not see the plaintext values. The authorized runtime may decrypt them. Which offered approach provides the additional client-side protection and key-access control?",
 "Rely only on default at-rest encryption and assume every console viewer is denied plaintext.|Move the function to EC2 because Lambda has no environment-variable encryption.|Use a suitable customer-managed KMS key and supported client-side encryption helpers, with runtime decryption permissions scoped separately.|Use ACM/CloudHSM SSL settings as the environment-variable storage control.",
 "At-rest encryption and permission to view or decrypt configuration are separate controls.",
 "Default storage encryption alone does not establish the specific separation of viewer and decrypt permissions.|Lambda supports environment-variable encryption; changing compute service does not inherently solve the access policy.|Client-side ciphertext and restricted KMS permissions support the stated separation when runtime decryption is implemented.|TLS certificate/HSM configuration is not the supported Lambda environment-value encryption-helper mechanism.",
 "This does not protect secrets from an actor who can change authorized function code or impersonate its runtime. Secrets Manager/Parameter Store retrieval is another architecture to evaluate when offered.")
r(21,"A","performance","Highly available Windows block access","ontap",
 "A Windows trading application will run on EC2 instances across two AZs. Its data interface requires block storage through iSCSI rather than an SMB share or object API. Which offered managed storage design supports the required multi-AZ architecture?",
 "Use a suitable Multi-AZ FSx for NetApp ONTAP filesystem and supported Windows iSCSI/multipath configuration.|Use FSx for Windows File Server as the iSCSI block target.|Use EFS and cross-Region replication as a Windows block device.|Use S3 buckets in individual AZs with cross-Region replication.",
 "ONTAP supplies supported iSCSI access; Windows file sharing and object storage are different interfaces.",
 "A supported ONTAP Multi-AZ and Windows iSCSI design provides the offered managed block-access pattern.|FSx for Windows exposes native SMB file sharing, not the stated iSCSI block target.|EFS is NFS file storage, not the Windows iSCSI device described.|S3 is regional object storage and does not expose the requested AZ-local bucket/block-device model.",
 "Validate supported multipath, failover, network, and application clustering configuration and benchmark latency; naming Multi-AZ alone does not configure every client.")
r(22,"A","performance","Parallel processing and cold objects","lustre s3",
 "A machine-learning training workload uses existing Lustre clients for high-throughput parallel access to active datasets. It also needs economical object storage for inactive datasets. Which offered pairing preserves that filesystem compatibility and supplies the cold object tier?",
 "FSx for Lustre for active parallel files and S3 for inactive objects.|EFS for active files and S3 for inactive objects.|FSx for Windows for active files and S3 for inactive objects.|FSx for Lustre and permanently provisioned io1 EBS volumes as the low-cost cold object archive.",
 "Pick hot-processing and cold-retention storage independently instead of buying the fastest tier for every copy.",
 "Lustre targets the stated client/parallel processing interface, and S3 provides object-storage classes for inactive data.|EFS supports many parallel shared-file workloads, but it is not the explicitly required Lustre-compatible filesystem.|A Windows SMB filesystem is not the Lustre interface requested by this workload.|Provisioned-IOPS block volumes are not the natural low-cost object-archive service.",
 "Study clarification makes existing Lustre compatibility explicit. Use supported data-repository integration and import/export/retention policies; S3 does not become a general POSIX filesystem.")
r(23,"D","performance","Windows shared-file migration","windows",
 "A company is migrating a Windows application, such as SharePoint or IIS, and its shared files to AWS. It needs native Windows file-sharing semantics, AD integration, and a managed multi-AZ option. Which offered service is the best fit?",
 "Create an NFS-only File Gateway share as the native Windows filesystem replacement.|Join an EFS filesystem to AD as a native SMB/NTFS service.|Mount an ordinary S3 bucket as if it supplied the complete Windows filesystem semantics.|Use FSx for Windows File Server with the supported AD and Multi-AZ configuration.",
 "Native SMB/NTFS, AD integration, and managed Multi-AZ support identify FSx for Windows File Server.",
 "The offered NFS share does not provide the required native Windows file-sharing feature set.|EFS does not turn into a native SMB/NTFS filesystem by naming an AD domain.|An S3 object API is not a transparent replacement for all required Windows filesystem semantics.|FSx for Windows supplies the supported Windows sharing, directory, and high-availability options.")
r(25,"C","secure","Temporary private object downloads","url",
 "A photo service discovers that unrestricted public S3 object URLs are being reused by other websites. It wants to remove public read access and issue short-lived download links only after its application authorizes a customer. Which offered change directly provides that access model?",
 "Move the files to WorkDocs as the S3 access-control mechanism.|Add CloudFront while keeping the origin unrestricted and issuing no access credentials.|Make the bucket private and issue appropriately scoped presigned URLs with expiry.|Use subnet NACLs to block the remote websites' referrer names.",
 "A private bucket and time-limited authorization links replace unrestricted public reads.",
 "WorkDocs is retired and is not the requested S3 access-control mechanism.|A CDN alone does not authorize customers or prevent direct public-origin access.|The application can authorize a user and issue a bounded signed request using suitable permissions.|NACLs do not inspect browser referrer names and are not attached to S3 buckets.",
 "Presigned URLs are bearer capabilities and can be shared or reused until expiry within their permissions. This is not absolute hotlink or redistribution prevention.")
r(26,"C","resilient","Guest metrics across operating systems","cw",
 "A company runs Linux and Windows EC2 workloads continuously. It needs guest memory utilization and filesystem-space metrics from every instance in CloudWatch. Which offered implementation supplies those measurements?",
 "Enable a nonexistent EC2 Enhanced Monitoring switch and assume no agent configuration is needed.|Use only default EC2 monitoring because it already reports every guest memory/filesystem metric.|Install and configure the unified CloudWatch agent with suitable instance permissions and metric settings.|Use Inspector vulnerability scans as the performance-metric collector.",
 "Guest memory and filesystem-space measurements need a collection mechanism; default EC2 metrics do not supply them all.",
 "Enhanced Monitoring is an RDS feature name and does not replace configured EC2 guest collection.|Default EC2 monitoring does not expose the requested guest memory and filesystem-space measurements.|A configured unified agent publishes supported OS measurements as CloudWatch metrics.|Vulnerability findings do not provide the requested continuous guest performance time series.")
r(27,"D","resilient","Synchronous RDS standby","rds",
 "A MySQL application currently uses one RDS DB instance in one AZ. It needs a traditional managed standby with synchronous replication and automatic instance failover in another AZ. Which offered configuration fits?",
 "Use a DynamoDB read replica for the MySQL database.|Add a traditional asynchronous RDS read replica only.|Run CloudFront as the database Multi-AZ replica.|Enable a traditional RDS Multi-AZ DB instance deployment.",
 "A traditional Multi-AZ DB instance standby provides synchronous replication; ordinary read replicas address different needs.",
 "DynamoDB does not supply a native MySQL read replica through this proposed operation.|A traditional RDS read replica normally uses asynchronous replication and is not this managed synchronous standby.|CloudFront is a content-delivery service rather than an RDS database standby.|This deployment supplies the supported synchronous standby and automatic failover pattern.",
 "This is specifically the DB instance deployment; Multi-AZ DB clusters have different replication and readable-instance behavior.")
r(28,"C","secure","PII discovery in object storage","macie",
 "A government portal stores supported census document types in S3 using supported server-side encryption. It needs sensitive-data findings for PII and notifications about relevant bucket/privacy risks. Which offered analysis service is appropriate?",
 "Use Polly to scan S3 object contents for sensitive-data patterns.|Use Kendra as the bucket threat and PII compliance scanner.|Configure Macie discovery and appropriate findings/notification integrations.|Use Fraud Detector as the general S3 object-content classifier.",
 "Macie classifies supported sensitive S3 content; speech, document search, and fraud scoring have different purposes.",
 "Polly synthesizes speech and is not the sensitive-object discovery service.|Kendra provides enterprise search, not this dedicated S3 sensitive-data discovery workflow.|Macie supplies supported discovery and findings that can feed the configured notification workflow.|Fraud scoring is not a substitute for the stated S3 content-classification capability.",
 "Grant the required S3/KMS permissions and configure supported data identifiers and formats. Classification findings alone do not prove application compliance or automatically prevent uploads.")
r(32,"B","secure","Corporate SAML federation","iam",
 "Employees authenticate to an existing corporate Active Directory and need federated AWS access using those identities. Which offered approach implements a supported SAML-based trust flow rather than duplicating IAM users?",
 "Create a VPC and assume network placement authenticates the employees.|Use an appropriate AD FS/SAML identity-provider integration and authorized IAM roles.|Treat social web identity federation as an interchangeable SAML provider.|Create a separate long-lived IAM user for each employee.",
 "Federation reuses an external identity; role trust and permissions still authorize AWS access.",
 "A VPC is a network boundary and does not itself establish the required identity federation.|A suitable SAML IdP, trust policy, and role permissions implement the offered corporate federation design.|Web identity and SAML are distinct trust protocols and cannot simply be substituted by name.|Duplicating users contradicts the requested use of the existing federated identity flow.",
 "IAM Identity Center is a current workforce SSO option to evaluate where offered. Directory connectivity and application federation still need configuration.")
r(33,"B","secure","Client-controlled encryption boundaries","client",
 "A medical application uploads sensitive objects to S3. The master key must remain under the client's control outside AWS, and plaintext object data must never be sent to AWS. Which encryption approach meets both requirements?",
 "Use client-side encryption with the master key held in AWS KMS.|Encrypt and decrypt locally with a client-held master key, then upload only ciphertext and appropriate encrypted-key metadata.|Upload plaintext over TLS and use SSE-KMS.|Supply the plaintext customer encryption key to S3 using SSE-C.",
 "When AWS must receive neither plaintext data nor the master key, encryption and master-key custody stay on the client side.",
 "This still places the master key in an AWS key-management service rather than entirely outside AWS.|The client controls the master key and sends encrypted object data rather than plaintext.|TLS protects transit, but S3 receives plaintext for server-side encryption.|SSE-C sends the supplied key to S3 for server-side cryptography, contrary to this custody requirement.")

r(41,"A","secure","AWS compliance evidence","artifact",
 "Auditors need AWS-issued SOC, PCI, and related compliance reports for the AWS services the company uses. Which offered service provides those documents?",
 "Use AWS Artifact to access the applicable AWS compliance reports.|Use Security Hub as the portal for downloading every AWS audit report.|Use Macie to retrieve SOC reports from ACM.|Run Inspector to download AWS's compliance attestations.",
 "Artifact supplies AWS compliance evidence; workload findings are a different output.",
 "Artifact is the supported self-service source for applicable AWS compliance documents.|Security Hub aggregates findings and controls rather than acting as the AWS report-download portal.|Macie classifies supported S3 content, and ACM manages certificates rather than SOC documents.|Inspector scans supported vulnerabilities rather than distributing AWS compliance attestations.",
 "An AWS report does not establish that the company's own application configuration and processes are compliant.")
r(44,"D","performance","Flexible NoSQL attributes","dynamo",
 "A high-traffic application uses key-based access, needs regional/global scalability, and frequently adds or changes non-key item attributes. It wants managed NoSQL storage without a relational schema migration for every optional attribute. Which offered service fits best?",
 "Amazon Redshift.|A traditional RDS relational DB instance.|Aurora with relational read replicas.|Amazon DynamoDB with appropriate key, capacity, and global-table design.",
 "Flexible item attributes do not remove the need to design stable keys and access patterns.",
 "A warehouse is not the requested high-traffic operational key-value/document database.|A relational instance targets a different schema and query model than the one explicitly described.|Read replicas add read capacity but do not change Aurora into the requested NoSQL access model.|DynamoDB supports flexible non-key attributes and managed capacity/replication options for appropriate workloads.",
 "Changing primary keys or adding some access patterns can require indexes, new tables, or migration. No service guarantees zero impact from every possible data-model change.")
r(45,"D","secure","Dedicated key-store control","keys",
 "A company wants KMS integrations while keeping key material in a customer-controlled dedicated HSM cluster. It must be able to disconnect that store to stop KMS cryptographic use and inspect supported HSM audit logs independently. Which offered design fits?",
 "Store KMS custom-key-store material as plaintext objects in S3.|Use an AWS-managed key and assume the customer controls its dedicated HSM cluster.|Use an AWS-owned key and assume the customer can administer its underlying HSM cluster.|Use a supported customer-managed KMS key in a CloudHSM custom key store.",
 "A CloudHSM custom key store combines KMS integration with customer administration of the backing cluster.",
 "An S3 plaintext key object is not the supported backing store of this KMS custom-key-store architecture.|An AWS-managed key does not give the customer the described dedicated cluster administration.|AWS-owned keys are not customer-administered custom-key-store resources.|A supported CloudHSM-backed custom store supplies the requested integration and disconnect/administration boundary.",
 "Study clarification replaces the supplied claim of immediate removal of all key copies with the supported disconnect control. Backups and KMS key-deletion waiting periods require separate handling.")
r(46,"A","cost","Automatic capacity targets","tracking",
 "An EC2 application should automatically add and remove capacity to maintain a measured utilization target without hand-authoring many scaling adjustment steps. Which offered policy is the most direct fit?",
 "Target tracking scaling.|Scheduled scaling without a workload metric.|Suspending scaling permanently.|A simple scaling adjustment without the requested maintained target.",
 "Target tracking expresses the desired metric level; AWS computes supported capacity adjustments.",
 "A supported target metric lets the policy adjust capacity toward the stated utilization objective.|A calendar schedule is useful for known times but does not itself maintain the requested measured target.|Suspending scaling prevents automatic adaptation and does not meet the capacity objective.|A simple adjustment is not the same as configuring a continuously maintained target.")
r(48,"A","resilient","Row changes versus database events","invoke",
 "A dealership uses a supported Aurora MySQL configuration. When a car is sold, application/database logic must remove the active listing and send processing work to SQS. Which offered integration can react to the business data change rather than only database-instance lifecycle events?",
 "Use appropriate application/stored-procedure logic with Aurora's supported Lambda integration, then let Lambda publish to SQS.|Use an RDS instance event subscription as if it emitted every sold-car row change directly to Lambda.|Subscribe SQS to RDS lifecycle events and assume SQS fans them out to SNS automatically.|Treat database-instance event subscriptions as a complete row-level change-data feed.",
 "Database-instance events and application row-change events are different signals.",
 "Supported Aurora MySQL Lambda invocation can connect explicit business/database logic to the queue publisher.|Instance events do not provide an automatic event for every business row update.|This confuses lifecycle notifications, message queues, and pub/sub delivery direction.|Instance event subscriptions are not a general row-level CDC mechanism.",
 "Coordinate commit, retries, and side effects carefully; an outbox/CDC architecture can be preferable for stronger delivery guarantees. Configure the supported engine integration and IAM/network access.")
r(49,"A","performance","Aurora read capacity","replicas",
 "An Aurora application has variable read traffic and uses supported Aurora Replicas through the reader endpoint. The team wants to adjust reader count automatically within configured bounds rather than maintain peak capacity all day. Which offered feature fits?",
 "Aurora replica auto scaling.|Aurora Global Database solely as a replacement for local reader-count scaling.|A cross-Region replica without a scaling policy.|A fixed larger cluster without automatic capacity adjustment.",
 "Reader-count scaling and cross-Region replication solve different primary problems.",
 "A suitable replica scaling policy adjusts supported reader capacity between the configured minimum and maximum.|Global replication adds a regional architecture and does not replace this local replica-count policy.|A remote replica alone does not implement the requested automatic local reader count.|A fixed larger configuration retains capacity planning and idle peak resources.",
 "Replica scaling takes time and is not automatic writer resizing. Configure metrics, limits, failover capacity, and application connection behavior.")
r(50,"A","resilient","Cross-Region relational recovery","global",
 "A compatible relational application needs a cross-Region recovery architecture targeting very low replication lag and rapid managed promotion after a primary-Region outage. Which offered service is specifically designed for this Aurora-compatible relational pattern?",
 "Aurora Global Database.|Amazon Timestream.|DynamoDB Global Tables as a drop-in relational engine.|A generic RDS PostgreSQL cross-Region replica with an unconditional sub-second lag guarantee.",
 "Use a compatible cross-Region database architecture, then test the complete recovery process.",
 "Aurora Global Database provides the targeted compatible relational replication and supported recovery operations.|A time-series engine does not provide the same relational compatibility and recovery architecture.|Global Tables is a NoSQL multi-Region design, not a drop-in relational database.|Ordinary asynchronous replica lag and end-to-end recovery are not unconditional timing guarantees.",
 "Clarified as a design target rather than a guaranteed one-second RPO/sub-minute RTO. Detection, promotion, application routing, and dependent services all affect recovery.")
r(52,"CD","secure","Private WORM object access","access lock",
 "Tax documents in S3 must be accessed only through a designated VPC-only access path. Protected object versions must remain WORM-protected while an authorized legal hold is active. Which two controls fit these requirements?",
 "Enable Object Lock while disabling bucket versioning.|Attach Network Firewall directly to the S3 bucket as its complete access policy.|Use a VPC-only S3 access point with bucket policies that enforce the intended exclusive access path.|Enable versioning/Object Lock and apply the required legal holds and least-privilege hold-management permissions.|Choose Glacier Instant Retrieval alone as the immutability control.",
 "Network-access policy and protected-version retention are separate layers.",
 "Object Lock depends on versioning; disabling it is not the required supported configuration.|Network Firewall is not a firewall attached directly to an S3 bucket instead of its policies.|A properly enforced VPC-only access-point path scopes supported access to the designated VPC.|Object Lock/legal holds protect the selected versions while the hold is active and properly governed.|A storage class does not itself prevent deletion or establish a legal hold.",
 "An access point alone does not block every alternative bucket access path. Legal holds can be removed by authorized principals; protecting a version does not forbid creating a newer version of the same key.")
r(53,"B","secure","Managed DDoS protection","shield",
 "A company needs a supported enhanced managed DDoS protection service for its public-facing AWS resources. Which offered service is specifically intended for DDoS mitigation rather than only network allow rules or findings?",
 "Use WAF request filtering alone as the complete defense against every network-layer DDoS attack.|Use Shield Advanced protections for supported resources and the appropriate response integrations.|Use security groups and NACLs alone as the complete managed DDoS mitigation service.|Use Firewall Manager without any actual Shield or filtering protections.",
 "Shield mitigates supported DDoS threats; policy managers and allow lists have different roles.",
 "WAF is useful for supported HTTP traffic but is not a universal replacement for network-layer DDoS protections.|Shield Advanced supplies the enhanced managed DDoS capabilities for appropriately protected resources.|Access rules are useful controls but are not the enhanced managed DDoS service described.|Central policy rollout does not substitute for enabling the relevant protections.",
 "Shield Standard already provides baseline protection. Advanced capabilities, resources, support, and cost-protection eligibility have specific conditions.")
r(55,"BE","cost","Multi-account resource sharing","ram",
 "A company wants to organize its AWS accounts centrally and share supported resources such as Transit Gateways, Resolver rules, and License Manager configurations across business units. Which two offered building blocks supply account organization and resource sharing?",
 "Use ParallelCluster as the multi-account organization service.|Use Resource Access Manager shares for the supported resources.|Use IAM permissions alone as if they created every resource-sharing relationship.|Use Control Tower alone as a substitute for all resource shares.|Use AWS Organizations to organize the accounts and enable the appropriate sharing integration.",
 "Organizations groups accounts; RAM shares supported resources without duplicating them.",
 "ParallelCluster manages suitable HPC clusters, not the account organization hierarchy.|RAM provides the supported resource-sharing relationships with intended principals.|Identity permission alone does not create every service's cross-account resource share.|Control Tower helps governance but is not a blanket replacement for configuring RAM shares.|Organizations supplies the central account structure and appropriate integration used by the sharing design.")
r(57,"A","secure","Role-based database tokens","auth",
 "An EC2 application must authenticate to a supported RDS MySQL database using short-lived tokens authorized by its instance role instead of a stored database password. Which offered database feature is required?",
 "Enable supported IAM database authentication and configure the database user, IAM permission, and TLS connection.|Enable TLS alone and assume it authenticates the database user using an IAM role.|Attach an instance role and assume the database automatically accepts signed tokens without enabling the feature.|Use a generic STS token directly as the MySQL password without the supported RDS authentication flow.",
 "An instance role grants AWS permissions; the database must also support and enable the token authentication flow.",
 "The supported feature connects the signed token and IAM permission to the configured database user.|TLS encrypts the connection but does not by itself configure this database-user authentication method.|A role alone does not turn on or configure database-native IAM authentication.|An arbitrary STS session token is not the RDS MySQL authentication token format.")
r(59,"D","performance","Protecting API backends","api",
 "An API Gateway/Lambda application expects a large public traffic surge. Its downstream systems have limited sustainable capacity. Which offered API control directly limits the request rate reaching the backend?",
 "Manually resize the servers underlying the managed API Gateway service.|Assume API Gateway's own scaling means downstream limits need no configuration.|Enable a nonexistent API Gateway Multi-AZ read replica as the request buffer.|Configure appropriate steady-state and burst throttling limits.",
 "A scalable front door does not mean an unlimited backend; throttle to the capacity the application can handle.",
 "Customers do not resize API Gateway's underlying managed servers through this mechanism.|The managed gateway can scale while its downstream database or external API remains constrained.|Database replica terminology does not describe an API Gateway request-rate control.|Throttling bounds supported incoming request rates and reduces overload passed downstream.",
 "Throttling is best-effort rather than an absolute hard concurrency guarantee. Clients need suitable retry/backoff behavior.")
r(60,"D","resilient","Default versus guest metrics","cw",
 "Which offered EC2 measurement normally requires guest-side/custom collection rather than being supplied by the standard EC2 metric set?",
 "Instance CPU utilization.|Supported instance-store disk read activity.|Network packet output.|Guest memory utilization.",
 "CPU/network and supported device activity differ from measurements inside the guest's memory and filesystems.",
 "CPUUtilization is part of the ordinary EC2 monitoring set.|Supported EC2 disk activity metrics exist; this is different from filesystem free space.|The EC2 metric set includes supported network packet activity.|Guest memory use normally needs the CloudWatch agent or another configured custom metric publisher.")
r(61,"CD","resilient","Managed Windows and Oracle migration","beanstalk dms rds",
 "A company is moving a compatible Windows/.NET application and an Oracle Standard Edition database to AWS. It wants a managed multi-AZ application/database architecture with minimal application redevelopment. Which two offered actions best fit?",
 "Rehost the complete Oracle server on EC2 as the managed-database destination.|Require a container rewrite and use ECS Anywhere as the regional deployment service.|Use DMS to migrate supported data to a suitable RDS for Oracle Multi-AZ deployment.|Deploy the compatible Windows/.NET application to an appropriately configured Beanstalk multi-AZ environment.|Require a .NET Core/Kubernetes rewrite even though a compatible managed platform is available.",
 "Reduce redevelopment by selecting compatible managed platforms, while configuring availability at both tiers.",
 "EC2 rehosting can be valid but retains database host operations rather than supplying the requested managed database.|The proposed rewrite/service description adds work without an explicit container requirement.|A suitable managed Oracle destination and supported migration task meet the database compatibility/HA objective.|Beanstalk can provision the compatible application environment with appropriate multi-AZ capacity and load balancing.|A mandatory rewrite conflicts with the goal when the existing application fits a supported platform.",
 "Assess platform/engine compatibility, licensing, schema/features, migration logging, and cutover. DMS moves supported data, not every Oracle application component automatically.")
r(62,"C","secure","Governed cross-account data lakes","lake",
 "Business accounts each own S3 datasets. Authorized users must query a centrally governed data lake using role-based cross-account access, without maintaining unnecessary duplicate copies. Which offered service directly supplies the data-lake permissions/catalog-sharing layer?",
 "Use Control Tower as the per-table data-lake permission engine.|Schedule Lambda to copy every dataset before considering permissions.|Use appropriate Lake Formation cross-account permissions, catalog/resource links, and supported sharing integrations.|Use Firehose delivery alone as the cross-account governance policy.",
 "Central governance can share access to data where it resides; it is not necessarily a physical copy into one account.",
 "Account governance does not replace fine-grained data-lake permissions and supported query access.|Copying data adds synchronization work and still requires a governance design.|Lake Formation supplies supported permissions/sharing mechanisms for the intended catalog and data access.|A delivery pipeline moves records but does not itself establish the requested role-based lake governance.")
r(63,"D","cost","Managed transfers with expiration","transfer s3",
 "A company wants confidential SFTP uploads to durable, encrypted object storage. Objects should become eligible for deletion after 30 days with minimal server management. Which offered architecture fits?",
 "Use Transfer Family with S3 but assume the SFTP server has a general object-retention deletion switch.|Manage an EC2 SFTP server and a cron-based deletion process.|Use EFS and assume its storage-tier lifecycle policy deletes files at 30 days.|Use an appropriate Transfer Family SFTP endpoint, encrypted S3 storage, and an S3 lifecycle expiration rule.",
 "Use the managed transfer endpoint for the protocol and the storage service's lifecycle for object expiration.",
 "The proposed server-retention switch is not the S3 object lifecycle mechanism.|A self-managed transfer server and scheduler add operations when a supported managed option fits.|EFS lifecycle tiering is not a general timed file-deletion policy.|The endpoint preserves the SFTP client workflow while S3 supplies encryption, durability, and supported expiration.",
 "Lifecycle deletion is asynchronous after eligibility, not a guaranteed exact-second retention deadline. Configure permissions, encryption access, version handling, and endpoint exposure appropriately.")
r(64,"C","resilient","Durable S3 event fanout","notifications",
 "S3 object-created/deleted events must reach two teams. Each team needs an independent durable queue, so its consumer can be temporarily unavailable without competing with the other consumer. Which offered fanout design is appropriate?",
 "Send S3 events directly to an SNS FIFO topic without another supported integration.|Configure overlapping identical S3 notification filters and assume both direct queue destinations are always accepted.|Send supported S3 notifications to an SNS Standard topic with a separate subscribed SQS queue per team.|Have the SQS queues poll the SNS topic instead of subscribing.",
 "Fanout copies the event to independent queues; competing workers on one queue do not each receive every event.",
 "Direct S3 event notifications do not support that FIFO topic target as stated.|Overlapping S3 notification configurations have restrictions; the proposed assumption is not a general fanout design.|A supported topic/queue subscription design gives each team its own retained work backlog.|SNS pushes to subscribed endpoints; SQS queues do not poll an SNS topic as a stream.",
 "Set bucket/topic/queue permissions, retries, retention, and consumer idempotency. Alternative EventBridge designs can also be valid when offered.")
r(65,"C","performance","Event-driven file conversion","glue notifications",
 "A company receives 2 GB CSV objects in S3 and must start managed CSV-to-Parquet conversion on each upload, writing results to another bucket. It wants a durable trigger path and minimal self-managed processing infrastructure. Which complete offered design best fits?",
 "Convert files in a custom Lambda processor and add an SFTP service solely to copy the output between S3 buckets.|Schedule only a Glue crawler and assume discovering a schema performs ETL immediately for every upload.|Use S3 notifications to SQS, a configured Lambda event source mapping that starts a Glue ETL job, and a job that writes Parquet to the target bucket.|Maintain an EC2 Spark cluster and custom Function URL invocation code for every uploaded object.",
 "A crawler describes data; an explicitly invoked ETL job transforms it.",
 "The custom processor and unnecessary SFTP hop add integration work for this managed conversion requirement.|A crawler does not itself convert CSV to Parquet, and periodic discovery is not the requested upload trigger.|The queue, invocation function, and Glue job specify the missing trigger-to-job link and the managed transformation.|The EC2 cluster and custom invocation add infrastructure management that the Glue job can avoid.",
 "Study repair explicitly supplies the job-invocation component missing from the source's SQS-to-Glue claim. Handle duplicate events/job starts, object arguments, IAM, and concurrency limits.")
r(68,"C","secure","VPC-local service access","endpoints",
 "A private EC2 instance requires private, same-Region access to S3 and DynamoDB without an internet egress path. It does not require hybrid access to those endpoints. Which offered mechanism directly provides this service connectivity?",
 "Create a Direct Connect circuit solely as the VPC-local service endpoint.|Use VPN CloudHub as the S3/DynamoDB endpoint service.|Configure suitable S3 and DynamoDB VPC endpoints, route tables, and policies.|Enable encryption at rest and assume it creates private routes.",
 "Encryption settings, hybrid circuits, and private service endpoints solve different problems.",
 "A dedicated hybrid circuit is not needed merely to create these VPC-local service paths.|CloudHub connects suitable VPN sites and is not the requested service endpoint mechanism.|Appropriate gateway endpoints provide the stated eligible private service paths without general NAT egress.|Encrypting stored data does not create a network route or an endpoint.")
r(69,"C","secure","Consistent web filtering across accounts","waf manager",
 "Several AWS accounts host ALB-backed web applications receiving SQL injection attempts. The organization wants suitable HTTP rules and centrally managed rollout to the relevant applications. Which offered design fits?",
 "Use GuardDuty as the inline SQL-injection filter and Security Hub as the rule-deployment engine.|Treat Network Firewall alone as an ALB-associated WAF web ACL.|Use suitable WAF managed/custom rules and Firewall Manager policies with the required organization/configuration prerequisites.|Use Macie to scan application software vulnerabilities and Audit Manager to distribute web ACLs.",
 "WAF supplies the HTTP control; Firewall Manager coordinates the organization-wide policy.",
 "Threat findings and aggregation do not provide the stated inline request filtering and rule distribution.|This does not specify the supported ALB web ACL and centralized WAF policy relationship.|The supported web ACL and policy rollout supply both requested layers.|S3 content classification and audit evidence are not the web request-filtering/deployment services.",
 "WAF reduces exposure but does not replace parameterized SQL and application remediation. Configure supported targets, Organizations/Config prerequisites, exceptions, and rule testing.")
r(168,"D","resilient","Partition-scoped stream ordering","kinesis",
 "A REST API receives ordered readings from each sensor. Readings for one sensor must be processed in their accepted stream order; sensors do not require one shared global order. Which offered design preserves this scope with managed stream consumption?",
 "Use an API authorizer as the data-ordering engine.|Write records to S3 and assume object notifications preserve a global processing order.|Use an SQS Standard queue without an ordering design.|Integrate the API with Kinesis Data Streams using a consistent sensor partition key and configure a supported Lambda consumer for ordered per-key processing.",
 "State the ordering scope and partition key; a managed stream does not imply universal global order.",
 "An authorizer controls access, not record ordering or downstream execution sequence.|Object notifications and independent function calls do not establish the stated per-sensor processing order.|Standard queues have at-least-once delivery and best-effort ordering, not the specified ordering guarantee.|Consistent partitioning and the appropriate stream consumer settings preserve the stated supported per-key order.",
 "Clarification makes partition-scoped ordering explicit. Producer ordering/retries, failure handling, and idempotency remain part of the design.")
r(169,"D","secure","Secrets injected into ECS tasks","secrets",
 "An ECS Fargate application must receive database credentials as environment variables without placing plaintext values in the task definition. Which offered configuration correctly retrieves encrypted Parameter Store values during task launch?",
 "Encrypt secrets with ACM and give the application task role the secret-injection responsibility.|Store credentials in ECS Anywhere and use Access Analyzer to encrypt them.|Store a task-definition JSON file in Aurora and assume that encrypts every runtime environment value.|Use SecureString parameters encrypted with KMS, grant the task execution role the required access, and reference parameter ARNs in the container secrets configuration.",
 "The execution role supports launch-time injection; the task role authorizes application code after launch.",
 "ACM certificates do not encrypt secret-store values and the proposed role conflates application and launch plumbing.|ECS Anywhere is not a credential vault, and Access Analyzer is not an encryption engine.|The proposal adds an unrelated database and does not describe the supported launch-time secret integration.|Supported secrets references and execution-role permissions let ECS retrieve the values without plaintext task-definition entries.",
 "The source's taskRoleArn/execution-role confusion is corrected. Injected values are available to the authorized container in plaintext; rotation does not automatically update an already running task.")
r(180,"D","resilient","Three-tier subnet isolation","subnets",
 "An internet-facing ALB fronts private application instances and a private database tier. The database must have its own subnets and custom route tables, separate from all other tiers. All three tiers must support a two-AZ highly available design. What is the minimum number of subnets for this stated architecture?",
 "2|3|4|6",
 "Three separate tiers across two AZs require six subnets: two public ALB, two private application, and two private database subnets.",
 "Two subnets cannot give three independently subnet-isolated tiers in each of two AZs.|Three subnets can separate tiers once, but do not provide each tier in two AZs.|Four subnets fit some two-tier layouts but omit one of the separately required tier pairs.|Two subnets per tier across three tiers gives the required total of six.",
 "The supplied explanation also counted six, but its selected index pointed to four. The independently reviewed key selects six. Security groups, routes, and tier failover still need configuration.")
r(196,"C","secure","Regional default block encryption","default",
 "A company wants eligible new EBS volumes in an AWS Region to be encrypted automatically, including new restores from unencrypted snapshots. Which offered account/Region configuration provides that default?",
 "Use asymmetric KMS keys as the EBS encryption key type.|Rely on every operator to request a symmetric key manually for each restore.|Enable EBS encryption by default in the relevant AWS Region and configure the appropriate default KMS key.|Enable an account-wide encryption-by-default switch separately on each existing unencrypted volume.",
 "EBS encryption by default is a regional setting for eligible new resources, not an in-place conversion of old volumes.",
 "EBS encryption uses supported symmetric encryption keys, not the proposed asymmetric key selection.|Manual per-volume configuration does not supply the requested automatic regional default.|The regional default applies to eligible new volumes and supported snapshot-derived volume creation.|This is not a separate in-place toggle that retroactively encrypts each existing volume.",
 "Existing unencrypted volumes/snapshots need an appropriate encrypted-copy/replacement workflow. Configure each required Region independently.")
r(228,"C","secure","Geographic content restrictions","edge",
 "A CloudFront distribution serves a private S3 origin using OAC. Licensing permits viewers in only specified countries, and denied viewers should receive a configured error page. Which offered change supplies the country-based viewer restriction?",
 "Use signed URLs/cookies alone and assume they identify the viewer's country.|Use a time-based IAM policy as the distribution's country allow list.|Configure CloudFront geographic restrictions with the appropriate allow list and supported custom error responses.|Create a nonexistent CloudFront Function URL as the country-filter feature.",
 "Origin access, viewer authorization, and country restrictions are separate controls.",
 "Signed capabilities can authorize content access but do not by themselves implement this geographic allow list.|A time restriction is not a country-based viewer filter.|The geographic policy supplies the country restriction while supported error configuration handles denied responses.|CloudFront Functions does not expose the proposed Lambda-style Function URL feature.",
 "IP geolocation is not perfect proof of physical location. OAC restricts origin access; it does not determine a viewer's licensing country.")

h(51,"AD Connector is a directory proxy, not by itself a complete AWS console federation flow. The offered pair omits the necessary supported SSO/IdP integration and trust setup; adding an IAM role alone does not specify how a developer obtains a federated console session.")
h(58,"The embedded IAM JSON is materially corrupted: actions, ARNs, braces, and resource scopes cannot be read reliably. The AI explanation infers a policy absent from the available source. Without an intact policy, selecting three allowed operations would fabricate the decisive facts.")
h(67,"Modern EKS already provides default envelope encryption for supported API data. The source does not require a customer-managed key or identify an older eligible cluster, and its choices mix control-plane etcd encryption with EBS CSI/secret-store features. The stated requirement does not uniquely establish the proposed extra encryption action.")
h(134,"The policy JSON and source CIDRs are corrupted and the prompt is truncated. The exact Allow/Deny actions, IP condition, and valid alternative address determine the answer; the AI reconstruction is not an independently verifiable policy from this file.")
h(153,"A compute placement group does not control the placement of FSx service endpoints or guarantee on-premises-to-cloud latency. The source combines local-network latency and multi-protocol storage without a complete connectivity/workload placement design, so the exact two choices cannot guarantee the stated result.")
h(157,"The licensing prohibition is expressed as an AWS Region ban, but the proposed Local Zone is an extension of that same parent Region. The source does not distinguish physical-location restrictions from parent-Region restrictions or establish an eligible zone/network path. A single-digit end-to-end latency guarantee is also unsupported.")
h(301,"The embedded NoSQL engine and required application access patterns are unspecified. DMS does not migrate every arbitrary embedded database into DynamoDB as a drop-in replacement. A supported source/target, schema/access assessment, and application migration plan are missing from the supposed complete answer.")

# A complete corrected counterpart can replace a previously defective unscored source.
RECOVERED_SOURCES = {682:"html-014"}

# Audited duplicates within the published bank. All old records remain available to
# grade historical sessions; only the canonical item is used for new study sessions.
BANK_DUPLICATES = [
 (160,240),(361,658),(363,717),(364,718),(367,714),(374,655),(381,680),
 (406,709),(417,708),(427,696),(432,726),(436,697),(449,719),(464,684),
 (516,660),(543,670),(544,673),(552,710),(564,691),(568,669),(569,686),
 (597,716),(636,649),(345,270),(820,560),
]
