## Network Rules

rule {
    description           = null
    destination_addresses = ["192.0.2.1", "192.0.2.2"]
    destination_fqdns     = []
    destination_ip_groups = []
    destination_ports     = ["*"]
    name                  = "Rule_1"
    protocols             = ["Any"]
    source_addresses      = ["198.51.100.1"]
    source_ip_groups      = []
}
rule {
    description           = null
    destination_addresses = ["198.51.100.1"]
    destination_fqdns     = []
    destination_ip_groups = []
    destination_ports     = ["*"]
    name                  = "Rule_2"
    protocols             = ["Any"]
    source_addresses      = ["192.0.2.1", "192.0.2.2"]
    source_ip_groups      = []
}
network_rule_collection {
    action   = "Allow"
    name     = "Connector"
    priority = 100
    rule {
        description           = null
        destination_addresses = ["*"]
        destination_fqdns     = []
        destination_ip_groups = []
        destination_ports     = ["*"]
        name                  = "Rule_3"
        protocols             = ["Any"]
        source_addresses      = ["192.0.2.3"]
        source_ip_groups      = []
    }
    rule {
        description           = null
        destination_addresses = ["*"]
        destination_fqdns     = []
        destination_ip_groups = []
        destination_ports     = ["*"]
        name                  = "Allow_ICMP_Local"
        protocols             = ["ICMP"]
        source_addresses      = ["198.51.100.0/24"]
        source_ip_groups      = []
    }
    rule {
        description           = null
        destination_addresses = ["192.0.2.3"]
        destination_fqdns     = []
        destination_ip_groups = []
        destination_ports     = ["22"]
        name                  = "Allow_SSH_Local"
        protocols             = ["Any"]
        source_addresses      = ["198.51.100.0/24"]
        source_ip_groups      = []
    }
    rule {
        description           = null
        destination_addresses = ["192.0.2.3"]
        destination_fqdns     = []
        destination_ip_groups = []
        destination_ports     = ["*"]
        name                  = "Allow_ICMP_External"
        protocols             = ["ICMP"]
        source_addresses      = ["*"]
        source_ip_groups      = []
    }
    rule {
        description           = null
        destination_addresses = ["192.0.2.4"]
        destination_fqdns     = []
        destination_ip_groups = []
        destination_ports     = ["*"]
        name                  = "Allow_DataBroker_Traffic"
        protocols             = ["Any"]
        source_addresses      = ["198.51.100.0/24"]
        source_ip_groups      = []
    }
    rule {
        description           = null
        destination_addresses = ["198.51.100.0/24"]
        destination_fqdns     = []
        destination_ip_groups = []
        destination_ports     = ["*"]
        name                  = "DataBroker_To_Internal"
        protocols             = ["Any"]
        source_addresses      = ["192.0.2.4"]
        source_ip_groups      = []
    }
    rule {
        description           = null
        destination_addresses = ["192.0.2.5"]
        destination_fqdns     = []
        destination_ip_groups = []
        destination_ports     = ["*"]
        name                  = "DataBroker_To_Storage"
        protocols             = ["Any"]
        source_addresses      = ["192.0.2.4"]
        source_ip_groups      = []
    }
    rule {
        description           = null
        destination_addresses = ["192.0.2.5"]
        destination_fqdns     = []
        destination_ip_groups = []
        destination_ports     = ["*"]
        name                  = "Storage_To_Cloud"
        protocols             = ["Any"]
        source_addresses      = ["198.51.100.0/24"]
        source_ip_groups      = []
    }
    rule {
        description           = null
        destination_addresses = ["192.0.2.6"]
        destination_fqdns     = []
        destination_ip_groups = []
        destination_ports     = ["*"]
        name                  = "Storage_To_DataCenter"
        protocols             = ["Any"]
        source_addresses      = ["192.0.2.5"]
        source_ip_groups      = []
    }
    rule {
        description           = null
        destination_addresses = ["192.0.2.5"]
        destination_fqdns     = []
        destination_ip_groups = []
        destination_ports     = ["*"]
        name                  = "DataCenter_To_Storage"
        protocols             = ["Any"]
        source_addresses      = ["192.0.2.6"]
        source_ip_groups      = []
    }
    rule {
        description           = null
        destination_addresses = ["192.0.2.7"]
        destination_fqdns     = []
        destination_ip_groups = []
        destination_ports     = ["*"]
        name                  = "Allow_FileSync_Server"
        protocols             = ["Any"]
        source_addresses      = ["198.51.0.0/16"]
        source_ip_groups      = []
    }
    rule {
        description           = null
        destination_addresses = ["198.51.0.0/16"]
        destination_fqdns     = []
        destination_ip_groups = []
        destination_ports     = ["*"]
        name                  = "FileSync_Backup"
        protocols             = ["Any"]
        source_addresses      = ["192.0.2.7"]
        source_ip_groups      = []
    }
}