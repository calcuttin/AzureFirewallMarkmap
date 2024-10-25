## DNAT Rules

nat_rule_collection {
    action   = "Dnat"
    name     = "sanitizedRuleCollection"
    priority = 100
    rule {
      destination_address = "203.0.113.1"
      destination_ports   = ["22"]
      name                = "Rule_1"
      protocols           = ["TCP"]
      source_addresses    = ["*"]
      translated_address  = "192.0.2.1"
      translated_port     = 22
    }
    rule {
      destination_address = "203.0.113.1"
      destination_ports   = ["21"]
      name                = "Rule_2"
      protocols           = ["TCP"]
      source_addresses    = ["*"]
      translated_address  = "192.0.2.1"
      translated_port     = 21
    }
    rule {
      destination_address = "203.0.113.2"
      destination_ports   = ["443"]
      name                = "Rule_3"
      protocols           = ["TCP"]
      source_addresses    = ["*"]
      translated_address  = "192.0.2.2"
      translated_port     = 443
    }
    rule {
      destination_address = "203.0.113.2"
      destination_ports   = ["80"]
      name                = "Rule_4"
      protocols           = ["TCP"]
      source_addresses    = ["*"]
      translated_address  = "192.0.2.2"
      translated_port     = 80
    }
    rule {
      destination_address = "203.0.113.3"
      destination_ports   = ["443"]
      name                = "Rule_5"
      protocols           = ["TCP"]
      source_addresses    = ["*"]
      translated_address  = "192.0.2.3"
      translated_port     = 443
    }
}