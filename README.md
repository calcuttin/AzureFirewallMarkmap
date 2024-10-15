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

```terraform
resource "firewall_rule" "internal_to_cloud" {
  name                  = "Internal_to_Cloud"
  action                = "allow"
  source_addresses      = ["192.168.1.0/24"]
  destination_addresses = ["10.0.0.1", "10.0.0.2"]
  protocols             = ["tcp", "udp"]
}

resource "firewall_rule" "cloud_to_internal" {
  name                  = "Cloud_to_Internal"
  action                = "allow"
  source_addresses      = ["10.0.0.1", "10.0.0.2"]
  destination_addresses = ["192.168.1.0/24"]
  protocols             = ["tcp"]
}

resource "firewall_rule" "block_external" {
  name                  = "Block_External_Access"
  action                = "deny"
  source_addresses      = ["0.0.0.0/0"]
  destination_addresses = ["192.168.1.10"]
  protocols             = ["tcp"]
}

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

# Create the Markmap-compatible markdown file, breaking it into sections of 25 rules per section
create_markmap(parsed_rules, output_markdown_file, rules_per_section=25)
