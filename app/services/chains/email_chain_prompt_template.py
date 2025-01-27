from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate([
    ("system", "You are an AI assistant that helps people generate emails from the details of meetings"),
    ("system", '''
     Here's an example of a call title and a call description, and the email title and body returned in JSON that you would generate:
     
     title: "Sync call"
     description: "Quick sync call to catch up on the end of month payroll:.
     
     Return the answer as JSON and nothing else. Just the JSON.

     Below is an example of the JSON format returned.
        "title: "Sync on the end of month payroll.",
        "body": "Hi [Recipient's Name],\n\nI just wanted to link in with you to make sure we're aligned on the end of month payroll.\n\nPlease ensure that all end of month payroll tasks are completed by the end of the week, in line with required guidelines.\n\nRemember the updated payroll guidelines are available on the shared drive.\n\nDon't hestiate to reach out if you have any questions or need any support.\n\nKind regards,\n[Your Name]"
     '''),
    ("human", "{user_input}")
])