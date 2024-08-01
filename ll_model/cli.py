import argparse
import os, sys
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from .LL_model import LL_model

def main():
    parser = argparse.ArgumentParser(description="LLama3 Model CLI")
    
    subparsers = parser.add_subparsers(dest="command")
    
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

    # Chat subcommand
    chat_parser = subparsers.add_parser('chat', help='Chat with the model')
    chat_parser.add_argument('--model_name',default='llama3', help='Name of the model')
    chat_parser.add_argument('--prompt', required=True, help='User prompt')
    chat_parser.add_argument('--system_message', help='System message')
    chat_parser.add_argument('--output_file', help='Output file')

    args = parser.parse_args()
    
    if args.command == 'create':
        LL_model.create(args.model_name, args.model_file, args.modelfilepath)
        print(f"Model {args.model_name} created successfully.")
    
    elif args.command == 'generate':
        print(f"Generating text with model {args.model_name}...")
        #model = LL_model(args.model_name)
        response = LL_model.generate(args.model_name,args.prompt, args.system_message,args.output_file)
        print(response)
    
    elif args.command == 'chat':
        #model = LL_model(args.model_name)
        response = LL_model.chat(args.model_name,args.prompt, args.system_message,args.output_file)
        print(response)

if __name__ == '__main__':
    main()
