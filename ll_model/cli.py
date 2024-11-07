import argparse
from .LL_model import LL_model
from ._config import OLLAMA_HOST
def main():
    parser = argparse.ArgumentParser(description="LLama3 Model CLI")
    
      

    subparsers = parser.add_subparsers(dest="command")
    # Add server_name argument
    parser.add_argument('--server_name', help='Server name or API address.')
    # Create subcommand
    create_parser = subparsers.add_parser('create', help='Create a new model')
    create_parser.add_argument('--model_name', required=True, help='Name of the model')
    create_parser.add_argument('--model_file', help='Path to the model file')
    create_parser.add_argument('--modelfilepath', help='Path to the model file directory')

    # Generate subcommand
    generate_parser = subparsers.add_parser('generate', help='Generate text from a prompt')
    generate_parser.add_argument('--model_name',nargs='?',const='llama3',default='llama3', help='Name of the model')
    generate_parser.add_argument('--prompt', required=True, help='Prompt for generation')
    generate_parser.add_argument('--system_message', help='System message')
    generate_parser.add_argument('--output_file', help='Output file')
    generate_parser.add_argument('--options', help='Other model parameters such as temperature')
    generate_parser.add_argument('--template',help="The prompt template to use")

    # Chat subcommand
    chat_parser = subparsers.add_parser('chat', help='Chat with the model')
    chat_parser.add_argument('--model_name',nargs='?',const='llama3',default='llama3', help='Name of the model')
    chat_parser.add_argument('--system_message', help='System message')
    chat_parser.add_argument('--output_file', help='Output file')

    args = parser.parse_args()
    if args.server_name:
        OLLAMA_HOST=args.server_name
    if args.command == 'create':
        LL_model.create(args.model_name, args.model_file, args.modelfilepath)
        print(f"Model {args.model_name} created successfully.")
    
    elif args.command == 'generate':
        print(f"Generating text with model {args.model_name}...")
        #model = LL_model(args.model_name)
        response = LL_model.generate(args.model_name,args.prompt, args.system_message,args.output_file, args.options, args.template)
        print(response)
    
    elif args.command == 'chat':
        #model = LL_model(args.model_name)
        response = LL_model.chat(args.model_name, args.system_message,args.output_file)
        print(response)

if __name__ == '__main__':
    main()
