# X00197631_CA2 - GAA match event tracker
## Overview
This project aimed to create a tool to enable the recording and tracking of events in a Gaelic Football match. I created the tool in Python and Azure DevOps to deploy it.

## Technologies Used
Python
Azure DevOps
git
GitHub
VSCode (interpreter)
*Dependencies*: Pylint, pytest, behave

## CI Foundations
Using the lab material I integrated pylint and unit testing into my Azure DevOps pipeline. I used a mixture of StackOverflow, ChatGPT and Reddit to assist me in setting up the pipeline, especially with the configuration of the YAML and .yml file for Python.

# X00197631 - CA3

## Testing Strategy
### Unit Tests
I used pytest to create the unit tests for this program. I was unsure of the use of Generative AI allowed at the time of making CA2, so I decided to write all unit tests by hand. I used ChatGPT to assist in giving me ideas of what unit tests could increase coverage but I wrote all of the unit tests myself, only using ChatGPT or Gemini to aid with detecting minor errors and bugs in my code (such as accidentally asserting different dtypes).

### Pylint
As per the spec's suggestion I used Pylint to generate static code coverage statistics on my work. Since I wrote all of the unit tests by hand in CA2 and my lack of unit tests written, I fell short of the 80% enforced code coverage.

### UAT
#### UAT writing
I used ChatGPT to aid in writing User Acceptance tests. I then corrected the errors from ChatGPT's generated code, as it got the order and format of outputs wrong. Initially it assumed player numbers were output as integers, that the events were output as dictionaries and that the events were only recorded in terms of outcomes (point, goal, wide) rather than including "shot" as the event, for example. I corrected all of these UATs to assert events correctly so that "shot" was asserted as it should be and added assertion for the outcome too to double-check it. I then wrapped the assertion for integers as a string so that it asserted player numbers correctly.
#### Integration with YAML

## CI Pipeline Implementation
### Multi-stage YAML configuration
I used the Lab material and Microsoft's tutorial on creating multi-stage pipelines (https://learn.microsoft.com/en-us/azure/devops/pipelines/process/create-multistage-pipeline?view=azure-devops) to tweak my yml file to split my pipeline into stages.

## Branch policies and protection
I removed the ability to force pushes to main and the ability to merge with main without a pull request or approval (self-approved via pull requests for this assignment).

## Troubleshooting Guide