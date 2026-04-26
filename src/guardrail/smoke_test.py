import os
import faulthandler
faulthandler.enable()

from dotenv import load_dotenv
load_dotenv()

from nemoguardrails import LLMRails, RailsConfig

print("Loading config...")
config = RailsConfig.from_path("src/guardrail/")
print("Config loaded.")

rails = LLMRails(config)
print("Rails loaded.")

print("\n--- Single Query Test ---")
response = rails.generate(messages=[{
    "role": "user",
    "content": "When will my card arrive?"
}])
print("Response:", response)

print("\n--- In-Scope Queries ---")
test_queries = [
    ("When will my card arrive?", "card_arrival"),
    ("My card is not working", "card_not_working"),
    ("The ATM swallowed my card", "card_swallowed"),
    ("My transfer failed", "failed_transfer"),
    ("How long does a transfer take?", "transfer_timing"),
    ("I want to cancel a transfer", "cancel_transfer"),
    ("My top up failed", "top_up_failed"),
    ("What are the top up limits?", "top_up_limits"),
    ("I need to verify my identity", "verify_my_identity"),
    ("Why do I need to verify my identity?", "why_verify_identity"),
]

for query, expected in test_queries:
    response = rails.generate(messages=[{"role": "user", "content": query}])
    print(f"Query   : {query}")
    print(f"Expected: {expected}")
    print(f"Response: {response}")
    print("-" * 60)

print("\n--- Out-of-Scope Queries ---")
oos_queries = [
    "What's the weather today?",
    "Can you help me write a poem?",
    "Who won the Champions League?",
    "How do I cook pasta?",
    "What's the capital of Japan?",
]

for query in oos_queries:
    response = rails.generate(messages=[{"role": "user", "content": query}])
    print(f"Query   : {query}")
    print(f"Response: {response}")
    print("-" * 60)

print("\n--- Confusable Intents ---")
confusable_queries = [
    ("My card payment was declined", "declined_card_payment"),
    ("My card is not being accepted at shops", "card_acceptance"),
    ("My card is not working", "card_not_working"),
    ("My transfer was declined", "declined_transfer"),
    ("My transfer failed", "failed_transfer"),
    ("I want to get a physical card", "get_physical_card"),
    ("I want to order a new card", "order_physical_card"),
]

for query, expected in confusable_queries:
    response = rails.generate(messages=[{"role": "user", "content": query}])
    print(f"Query   : {query}")
    print(f"Expected: {expected}")
    print(f"Response: {response}")
    print("-" * 60)

print("\n--- Threshold Edge Cases ---")
threshold_queries = [
    "I lost my card",
    "help",
    "I have a problem",
    "something is wrong",
    "my account",
]

for query in threshold_queries:
    response = rails.generate(messages=[{"role": "user", "content": query}])
    print(f"Query   : {query}")
    print(f"Response: {response}")
    print("-" * 60)