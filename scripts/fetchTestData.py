import re

def extract_data_from_text(text):
    descriptions = []
    expected_results = []

    # Split text into sections based on bullet points
    sections = re.split(r'•\s*', text)
    # Remove empty sections
    sections = [section.strip() for section in sections if section.strip()]

    for section in sections:
        # Extract description and expected result using regex
        match = re.search(r'Description:\s*(.*?)\s*Expected Result:\s*(.*?)\s*', section, re.DOTALL)
        if match:
            descriptions.append(match.group(1).strip())
            expected_results.append(match.group(2).strip())

    return descriptions, expected_results

# Your text data
text_data = """
    • Triggering the Pop-up:
        ◦ Description: Click on "View Connections" option under "Actions" column for a specific legislation.
        ◦ Expected Result: The pop-up window titled "View Connections" should appear overlaying the main page.
    • Display of Risks Table:
        ◦ Description: Verify that the Risks table is displayed in the pop-up window.
        ◦ Expected Result: All associated risks with their relevant details should be visible in a table format.
    • Display of Legal Items Table:
        ◦ Description: Verify that the Legal Items table is displayed in the pop-up window.
        ◦ Expected Result: All associated legal items with their relevant details should be visible in a table format.
    • Navigating Risks and Legal Items Tables:
        ◦ Description: Check if each table is clearly labeled for easy navigation.
        ◦ Expected Result: The Risks table and Legal Items table should have clear labels for easy identification.
    • Access to Mitigations from Risks Table:
        ◦ Description: Click on "View Controls" option in the Risks table for a risk.
        ◦ Expected Result: A pop-up window should open, displaying the mitigations for the selected risk.
    • Edit and Delete Options in Risks Table:
        ◦ Description: Check the presence and functionality of "Edit" and "Delete" options in the Risks table.
        ◦ Expected Result: The user should be able to edit or delete risks using the provided options.
    • Export Risks Table Data:
        ◦ Description: Click on the export option in the Risks table.
        ◦ Expected Result: Risks table data should be exported in CSV format successfully.
    • Access to Mitigations from Legal Items Table:
        ◦ Description: Click on "Controls" option in the Legal Items table for a legal item.
        ◦ Expected Result: A pop-up window should open, displaying the mitigations for the selected legal item.
    • Edit and Delete Options in Legal Items Table:
        ◦ Description: Check the presence and functionality of "Edit" and "Delete" options in the Legal Items table.
        ◦ Expected Result: The user should be able to edit or delete legal items using the provided options.
    • Export Legal Items Table Data:
        ◦ Description: Click on the export option in the Legal Items table.
        ◦ Expected Result: Legal Items table data should be exported in CSV format successfully.
    • Vertical Scrollbar and Entry Count:
        ◦ Description: Check if a vertical scrollbar appears and total entry count is displayed at the bottom of each table.
        ◦ Expected Result: Vertical scrollbar should appear when there are more entries than the visible area, and the total count of entries should be displayed accurately.
    • Closing the Pop-up:
        ◦ Description: Click on the close option in the pop-up window.
        ◦ Expected Result: The pop-up window should close seamlessly, returning the user to the main page.
    • Opening Mitigations Pop-up from Risks Table:
        ◦ Description: Click on "View Controls" option for a risk in the Risks table.
        ◦ Expected Result: A pop-up window titled "Mitigations for [Risk]" should open, displaying the mitigations for the selected risk.
    • Opening Mitigations Pop-up from Legal Items Table:
        ◦ Description: Click on "Controls" option for a legal item in the Legal Items table.
        ◦ Expected Result: A pop-up window titled "Mitigations for [Legal Item]" should open, displaying the mitigations for the selected legal item.
    • Edit Mitigations:
        ◦ Description: Try to edit the mitigations in the pop-up window.
        ◦ Expected Result: The user should be able to edit the mitigations for the selected risk or legal item.
    • Add Mitigations:
        ◦ Description: Try to add new mitigations in the pop-up window.
        ◦ Expected Result: The user should be able to add new mitigations for the selected risk or legal item.
    • Delete Mitigations:
        ◦ Description: Try to delete existing mitigations in the pop-up window.
        ◦ Expected Result: The user should be able to delete existing mitigations for the selected risk or legal item.
    • Closing the Mitigations Pop-up:
        ◦ Description: Click on the close option in the Mitigations pop-up window.
        ◦ Expected Result: The Mitigations pop-up window should close seamlessly.
"""

# Extract descriptions and expected results
descriptions, expected_results = extract_data_from_text(text_data)

# Print extracted data
for i in range(len(descriptions)):
    print(f"Description {i+1}: {descriptions[i]}")
    print(f"Expected Result {i+1}: {expected_results[i]}")
    print()
