*** Settings ***
Library    OperatingSystem

*** Variables ***
${SEARCH}    Biden
${SECTION}    Blogs,Business
${TYPE}    Article
${MONTHS}    2

*** Tasks ***
Convert to Work Items
    [Documentation]    Convert values from config.ini into work items
    @{sections}    Create List    ${SECTION}
    : FOR    ${section}    IN    @{sections}
    \    Log    Creating work item for section: ${section}
    \    Set work item variables    SEARCH=${SEARCH}    SECTION=${section}    TYPE=${TYPE}    MONTHS=${MONTHS}
    \    Save Work Item
