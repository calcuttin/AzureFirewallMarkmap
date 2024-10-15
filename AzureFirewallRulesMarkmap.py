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
        'source_addresses': re.compile(r'source_addresses\s*=\s*\[([^\]]+)\]'),
        'destination_addresses': re.compile(r'destination_addresses\s*=\s*\[([^\]]+)\]'),
        'protocols': re.compile(r'protocols\s*=\s*\[([^\]]+)\]'),
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
input_file_path = 'FilePathHERE'  # Replace with your actual file path
output_markdown_file = 'firewall_rules_markmap_limit25.md'  # This will be the output for Markmap

# Parse the rules
parsed_rules = parse_markdown_rules(input_file_path)

# Create the Markmap-compatible markdown file, breaking it into sections of 25 rules per section
create_markmap(parsed_rules, output_markdown_file, rules_per_section=25)
