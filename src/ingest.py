import os
import json
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter

# Load environment variables
load_dotenv()

def load_and_chunk_data():
    documents = []  # that will collect all chunks from all 3 files
    print("Loading and processing raw data...")
    
    # 1. Process Company Policies (Markdown) ---> file 1
    policy_path = "data/raw/company_policies.md"
    if os.path.exists(policy_path):
        with open(policy_path, "r", encoding="utf-8") as f:
            markdown_text = f.read()
        
        headers_to_split_on = [("##", "section")]
        markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
        md_chunks = markdown_splitter.split_text(markdown_text)
        
        for chunk in md_chunks:
            chunk.metadata["source"] = "company_policies.md"
            chunk.metadata["type"] = "policy"
        documents.extend(md_chunks)
        print(f"Loaded {len(md_chunks)} policy sections.")

    # 2. Process Products Catalog (JSON)
    product_path = "data/raw/products_catalog.json"
    if os.path.exists(product_path):
        with open(product_path, "r", encoding="utf-8") as f:
            products = json.load(f)
            
        for prod in products:
            prod_text = (
                f"Product Name: {prod['name']}\n"
                f"Category: {prod['category']}\n"
                f"Price: {prod['price_egp']} EGP\n"
                f"Stock Status: {'In Stock' if prod['in_stock'] else 'Out of Stock'}\n"
                f"Description: {prod['description']}"
            )
            
            doc = Document(
                page_content=prod_text,
                metadata={
                    "source": "products_catalog.json",
                    "type": "product",
                    "product_id": prod["id"],
                    "price_egp": prod["price_egp"],
                    "in_stock": prod["in_stock"],
                    "category": prod["category"]
                }
            )
            documents.append(doc)
        print(f"Loaded {len(products)} products with metadata.")
            
    # 3. Process Support FAQs (Text)
    faq_path = "data/raw/support_faqs.txt"
    if os.path.exists(faq_path):
        with open(faq_path, "r", encoding="utf-8") as f:
            faq_text = f.read()
        
        faq_items = faq_text.split("Q: ")
        faq_chunks = []
        for item in faq_items:
            if item.strip():
                doc = Document(
                    page_content="Q: " + item.strip(),
                    metadata={"source": "support_faqs.txt", "type": "faq"}
                )
                faq_chunks.append(doc)
        documents.extend(faq_chunks)
        print(f"Loaded {len(faq_chunks)} FAQ items.")
        
    print(f"\nTotal processed chunks ready for embedding: {len(documents)}")
    return documents  # <--- دي كانت ناقصة تماماً!

if __name__ == "__main__":
    docs = load_and_chunk_data()
    if docs:
        print("\n--- Sample Document Preview (Product Chunk) ---")
        sample_doc = docs[4] if len(docs) > 4 else docs[0]
        print(sample_doc.page_content)
        print("Metadata:", sample_doc.metadata)