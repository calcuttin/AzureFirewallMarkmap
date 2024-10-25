# Firewall Rules Mind Map Generator

This project provides a Python script that parses firewall rules from a markdown file and generates an interactive mind map using **Markmap**. The mind map will break the firewall rules into manageable sections (e.g., 25 or 50 rules per section) to improve readability.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Sample Firewall Rules (Terraform-style)](#sample-firewall-rules-terraform-style)
- [Instructions](#instructions)
  - [1. Parse Firewall Rules](#1-parse-firewall-rules)
  - [2. Generate Markmap](#2-generate-markmap)
  - [3. Rendering the Mind Map](#3-rendering-the-mind-map)
- [Customization](#customization)
- [Destination NAT](#destination-nat-rules)

## Overview

This Python script reads firewall rules from a markdown file, processes them, and outputs a new markdown file formatted for **Markmap**. The generated mind map breaks the firewall rules into sections to make them easier to read and visualize.

### Key Features:
- Parses firewall rules from markdown files.
- Supports breaking the rules into sections (e.g., 25 or 50 rules per section).
- Outputs a Markmap-compatible markdown file.
- Easily rendered as an interactive mind map using **Markmap CLI** or **Visual Studio Code**.

## Requirements

- **Python 3.x**: Make sure you have Python installed.
- **Markmap CLI** or **Markmap extension** for rendering the markdown as a mind map.

## Sample Firewall Rules (Terraform-style)

Below is an example of firewall rules written in a Terraform-style format. The Python script parses markdown files similar to this format, extracting relevant information such as `source_addresses`, `destination_addresses`, `protocols`, and `actions`.

```markdown
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
```
The above rules define various firewall policies, such as allowing or denying traffic between internal and cloud networks or blocking external access.

## Instructions

### 1. Parse Firewall Rules

The parse_markdown_rules() function reads a markdown file containing firewall rules and extracts the relevant data such as source addresses, destination addresses, protocols, and actions.

### 2. Generate Markmap

The create_markmap() function generates a Markmap-compatible markdown file. You can break down the rules into smaller sections for easier visualization (e.g., 25 or 50 rules per section).

Python Script

Here’s the Python script that you can use to parse firewall rules and generate a mind map using Markmap:

```python
import re

# Function to parse the firewall rules from the markdown file
def parse_markdown_rules(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Define a regex pattern to extract firewall rule attributes from the markdown
    rule_pattern = re.compile(r'rule\s*{(.*?)}', re.DOTALL)
    rules = rule_pattern.findall(content)
    
    parsed_rules = []
    
    # Regex patterns to extract specific rule fields
    field_patterns = {
        'name': re.compile(r'name\s*=\s*"(.+?)"'),
        'source_addresses': re.compile(r'source_addresses\s*=\s*$begin:math:display$([^$end:math:display$]+)\]'),
        'destination_addresses': re.compile(r'destination_addresses\s*=\s*$begin:math:display$([^$end:math:display$]+)\]'),
        'protocols': re.compile(r'protocols\s*=\s*$begin:math:display$([^$end:math:display$]+)\]'),
        'action': re.compile(r'action\s*=\s*"(.+?)"')
    }
    
    for rule in rules:
        rule_data = {}
        for key, pattern in field_patterns.items():
            match = pattern.search(rule)
            if match:
                rule_data[key] = match.group(1).strip()
                # Clean up arrays
                if key in ['source_addresses', 'destination_addresses', 'protocols']:
                    rule_data[key] = [addr.strip().strip('"') for addr in rule_data[key].split(',')]
        parsed_rules.append(rule_data)
    
    return parsed_rules

# Function to generate markdown for Markmap visualization, divided into sections
def create_markmap(parsed_rules, output_file, rules_per_section=25):
    with open(output_file, 'w') as file:
        # Write the header for the Markmap
        file.write("# Firewall Rules Mind Map\n\n")
        
        # Break the rules into sections
        total_rules = len(parsed_rules)
        sections = [parsed_rules[i:i + rules_per_section] for i in range(0, total_rules, rules_per_section)]
        
        # Write each section and its rules
        for section_num, section in enumerate(sections, start=1):
            file.write(f"## Section {section_num} (Rules {((section_num-1)*rules_per_section)+1} - {min(section_num*rules_per_section, total_rules)})\n\n")
            
            for rule in section:
                file.write(f"### Rule: {rule.get('name', 'N/A')}\n")
                file.write(f"- Action: {rule.get('action', 'N/A')}\n")
                file.write(f"- Protocols: {', '.join(rule.get('protocols', []))}\n")
                file.write(f"- Source Addresses:\n")
                for src in rule.get('source_addresses', []):
                    file.write(f"  - {src}\n")
                file.write(f"- Destination Addresses:\n")
                for dest in rule.get('destination_addresses', []):
                    file.write(f"  - {dest}\n")
                file.write("\n")
    print(f"Markdown output written to {output_file}")

# Path to your markdown file and the output markdown file for Markmap
input_file_path = 'parsedfiles.md'  # Replace with your actual file path
output_markdown_file = 'firewall_rules_markmap.md'  # This will be the output for Markmap

# Parse the rules
parsed_rules = parse_markdown_rules(input_file_path)
```
## 3. Rendering the Mind Map

Once the markdown file is generated, you can render the mind map in one of the following ways:

## Option 1: Use Markmap CLI

  ### 1.	Install Markmap CLI globally:
 ```bash
npm install -g markmap-cli
```
 ### 2.	Open the generated markdown file:
 ```bash
markmap firewall_rules_markmap.md
```
This will open the mind map in your default browser.

## Option 2: Use Visual Studio Code with Markmap Extension

1. Install the [Markmap extension](https://marketplace.visualstudio.com/items?itemName=gera2ld.markmap-vscode) in Visual Studio Code.
2. Open the firewall_rules_markmap.md file in VSCode.
3. Right-click and select Markmap: Open Preview to view the mind map.

# Customization

•	Adjust Rules per Section: You can modify the rules_per_section parameter in the create_markmap() function to control how many rules appear in each section
```python
create_markmap(parsed_rules, output_markdown_file, rules_per_section=50)
```
Render Formats: You can adjust the Markmap output format (SVG, PNG, etc.) using Markmap’s CLI options.
<img width="1020" alt="firewallex" src="https://github.com/user-attachments/assets/559893f0-9218-4239-9c9b-a6cb18e5e156">



# Destination NAT Rules
## Sample Destination NAT Rules (Sanitized Markdown-style)

Below is an example of sanitized DNAT rules written in markdown format. The Python script parses files similar to this format, extracting relevant information such as `destination_address`, `translated_address`, `translated_port`, `protocols`, and `action`.

```markdown
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
```
## Instructions

### 1. Parse DNAT Rules

The parse_markdown_rules() function reads a markdown file containing DNAT rules and extracts the relevant data such as destination addresses, protocols, and translated addresses.




### 2. Generate Markmap

The create_markmap() function generates a Markmap-compatible markdown file. You can break down the rules into smaller sections for easier visualization (e.g., 25 or 50 rules per section).

Python Script

Here’s the Python script that you can use to parse DNAT rules and generate a mind map using Markmap:
```python
import re

# Function to parse the DNAT rules from the markdown file
def parse_markdown_rules(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Define a regex pattern to extract DNAT rule attributes from the markdown
    rule_pattern = re.compile(r'rule\s*{(.*?)}', re.DOTALL)
    rules = rule_pattern.findall(content)
    
    parsed_rules = []
    
    # Regex patterns to extract specific rule fields
    field_patterns = {
        'name': re.compile(r'name\s*=\s*"(.+?)"'),
        'source_addresses': re.compile(r'source_addresses\s*=\s*$begin:math:display$([^$end:math:display$]+)\]'),
        'destination_address': re.compile(r'destination_address\s*=\s*"(.+?)"'),
        'destination_ports': re.compile(r'destination_ports\s*=\s*$begin:math:display$([^$end:math:display$]+)\]'),
        'protocols': re.compile(r'protocols\s*=\s*$begin:math:display$([^$end:math:display$]+)\]'),
        'action': re.compile(r'action\s*=\s*"(.+?)"'),
        'translated_address': re.compile(r'translated_address\s*=\s*"(.+?)"'),
        'translated_port': re.compile(r'translated_port\s*=\s*(\d+)')
    }
    
    for rule in rules:
        rule_data = {}
        for key, pattern in field_patterns.items():
            match = pattern.search(rule)
            if match:
                rule_data[key] = match.group(1).strip()
                # Clean up arrays
                if key in ['source_addresses', 'destination_ports', 'protocols']:
                    rule_data[key] = [addr.strip().strip('"') for addr in rule_data[key].split(',')]
        parsed_rules.append(rule_data)
    
    return parsed_rules

# Function to generate markdown for Markmap visualization, divided into sections
def create_markmap(parsed_rules, output_file, rules_per_section=25):
    with open(output_file, 'w') as file:
        # Write the header for the Markmap
        file.write("# DNAT Rules Mind Map\n\n")
        
        # Break the rules into sections
        total_rules = len(parsed_rules)
        sections = [parsed_rules[i:i + rules_per_section] for i in range(0, total_rules, rules_per_section)]
        
        # Write each section and its rules
        for section_num, section in enumerate(sections, start=1):
            file.write(f"## Section {section_num} (Rules {((section_num-1)*rules_per_section)+1} - {min(section_num*rules_per_section, total_rules)})\n\n")
            
            for rule in section:
                file.write(f"### Rule: {rule.get('name', 'N/A')}\n")
                file.write(f"- Action: {rule.get('action', 'N/A')}\n")
                file.write(f"- Protocols: {', '.join(rule.get('protocols', []))}\n")
                file.write(f"- Source Addresses:\n")
                for src in rule.get('source_addresses', []):
                    file.write(f"  - {src}\n")
                if 'destination_address' in rule:
                    file.write(f"- Destination Address: {rule['destination_address']}\n")
                if 'destination_ports' in rule:
                    file.write(f"- Destination Ports: {', '.join(rule.get('destination_ports', []))}\n")
                if 'translated_address' in rule:
                    file.write(f"- Translated Address: {rule['translated_address']}\n")
                if 'translated_port' in rule:
                    file.write(f"- Translated Port: {rule['translated_port']}\n")
                file.write("\n")
    print(f"Markdown output written to {output_file}")

# Path to your markdown file and the output markdown file for Markmap
input_file_path = 'dnat_rules.md'  # Replace with your actual file path
output_markdown_file = 'dnat_rules_markmap.md'  # This will be the output for Markmap

# Parse the rules
parsed_rules = parse_markdown_rules(input_file_path)

# Create the Markmap-compatible markdown file, breaking it into sections of 25 rules per section
create_markmap(parsed_rules, output_markdown_file, rules_per_section=25)
```
<img width="1265" alt="dnatex" src="https://github.com/user-attachments/assets/bb8c3e1a-0b7f-4364-bf66-9ff6d7d4cd64">
