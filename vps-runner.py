import ansible_runner

# Path to your Ansible playbook
playbook_path = "vps_playbook.yaml"

# Create an instance of AnsibleRunner and run it
ansible_runner.run(private_data_dir='.', playbook=playbook_path,)
