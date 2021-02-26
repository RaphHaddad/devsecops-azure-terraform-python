#!/usr/bin/env python3
import sys, subprocess, argparse

def execute_terraform_command(command):
    to_be_executed = f'terraform {command}'
    print(f'Executing command:\n{to_be_executed}')
    output = subprocess.run(to_be_executed, capture_output=True, text=True, shell=True)
    if output.stderr:
        print(output.stderr)
        sys.exit(1)
    return output.stdout, output.stderr

def terraform_init(resource_group_name):
    output, error = execute_terraform_command("init " +
                              f" -backend-config='path=.terraform-state-{resource_group_name}/{resource_group_name}.tfstate'" +
                              " -reconfigure"
                              f" --input=false")
    if error:
        sys.exit(1)
        print(error)
    else:
        print(output)

def generate_variable_string(terraform_variables):
    return ' '.join([ f"-var='{key}={terraform_variables[key]}'" for key in terraform_variables])

def terraform_plan(terraform_variables = {}):
    variable_command_section = generate_variable_string(terraform_variables)
    plan_result, error = execute_terraform_command(f"plan {variable_command_section} --input=false")

    if error:
        print_red(f"\n{error}\n")
        sys.exit(1)

    print(plan_result)

def terraform_apply(terraform_variables = {}):
    variable_command_section = generate_variable_string(terraform_variables)
    plan_result, error = execute_terraform_command(f"apply {variable_command_section} -auto-approve --input=false")

    if error:
        print_red(f"\n{error}\n")
        sys.exit(1)

    print(plan_result)

def parse_arguments():
    parser = argparse.ArgumentParser("Setup environment")
    parser.add_argument('--resource-group-name', '-rg',
                        type=str,
                        help="The resource group name to provission with the service connection.",
                        required=True)
    parser.add_argument('--azure-devops-project-name', '-pn',
                    type=str,
                    help="The project name to where the service connection will be provisioned.",
                    required=True)
    return parser.parse_args()

def main():
    cli_arguments = parse_arguments()
    resource_group_name = cli_arguments.resource_group_name
    project_name = cli_arguments.azure_devops_project_name
    terraform_init(resource_group_name)

    terraform_variables = {'resource-group-name': resource_group_name,
                           'azure-devops-project-name': project_name}
    terraform_plan(terraform_variables)
    terraform_apply(terraform_variables)

main()