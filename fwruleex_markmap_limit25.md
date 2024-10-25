# Firewall Rules Mind Map

## Section 1 (Rules 1 - 14)

### Rule: Rule_1
- Action: N/A
- Protocols: Any
- Source Addresses:
  - 198.51.100.1
- Destination Addresses:
  - 192.0.2.1
  - 192.0.2.2

### Rule: Rule_2
- Action: N/A
- Protocols: Any
- Source Addresses:
  - 192.0.2.1
  - 192.0.2.2
- Destination Addresses:
  - 198.51.100.1

### Rule: Rule_3
- Action: N/A
- Protocols: Any
- Source Addresses:
  - 192.0.2.3
- Destination Addresses:
  - *

### Rule: Allow_ICMP_Local
- Action: N/A
- Protocols: ICMP
- Source Addresses:
  - 198.51.100.0/24
- Destination Addresses:
  - *

### Rule: Allow_SSH_Local
- Action: N/A
- Protocols: Any
- Source Addresses:
  - 198.51.100.0/24
- Destination Addresses:
  - 192.0.2.3

### Rule: Allow_ICMP_External
- Action: N/A
- Protocols: ICMP
- Source Addresses:
  - *
- Destination Addresses:
  - 192.0.2.3

### Rule: Allow_DataBroker_Traffic
- Action: N/A
- Protocols: Any
- Source Addresses:
  - 198.51.100.0/24
- Destination Addresses:
  - 192.0.2.4

### Rule: DataBroker_To_Internal
- Action: N/A
- Protocols: Any
- Source Addresses:
  - 192.0.2.4
- Destination Addresses:
  - 198.51.100.0/24

### Rule: DataBroker_To_Storage
- Action: N/A
- Protocols: Any
- Source Addresses:
  - 192.0.2.4
- Destination Addresses:
  - 192.0.2.5

### Rule: Storage_To_Cloud
- Action: N/A
- Protocols: Any
- Source Addresses:
  - 198.51.100.0/24
- Destination Addresses:
  - 192.0.2.5

### Rule: Storage_To_DataCenter
- Action: N/A
- Protocols: Any
- Source Addresses:
  - 192.0.2.5
- Destination Addresses:
  - 192.0.2.6

### Rule: DataCenter_To_Storage
- Action: N/A
- Protocols: Any
- Source Addresses:
  - 192.0.2.6
- Destination Addresses:
  - 192.0.2.5

### Rule: Allow_FileSync_Server
- Action: N/A
- Protocols: Any
- Source Addresses:
  - 198.51.0.0/16
- Destination Addresses:
  - 192.0.2.7

### Rule: FileSync_Backup
- Action: N/A
- Protocols: Any
- Source Addresses:
  - 192.0.2.7
- Destination Addresses:
  - 198.51.0.0/16

