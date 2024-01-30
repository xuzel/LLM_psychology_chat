# Proposal

[toc]

# 1. Project topic

**Topic: Soul-Bridge Chat**

Our goal is to develop a dialogue-based psychological diagnosis and assessment system, which aims to identify users' personality traits and potential mental health issues through interaction with a Large Language Model (LLM). By analyzing the content, linguistic expressions, and response patterns in users' conversations, the system will be able to infer their emotional states, levels of psychological stress, and potential mental health risks. Additionally, the system will utilize these dialogues to provide users with preliminary psychological support and stress relief, helping them better understand and manage their emotions and mental health.

Our system will also include a series of customized mental health assessment tools and self-help strategies, designed to provide personalized mental health analysis and intervention suggestions. Users can access these tools through their daily conversations, making mental health assessments more seamless and natural. The design of our system focuses on protecting user privacy and data security, ensuring that all personal information is properly handled and encrypted.

# 2. Team members

| Name   | Student ID |
| ------ | ---------- |
| 徐则灵 | 1210022239 |
| 侯歌扬 | 1210032104 |
| 任正非 | 1210017801 |

# 3. Background

## 3.1 心理学问题调研

讲现在心理问题巴拉布拉，现在有多少人紫砂巴拉巴拉

## 3.2 现有技术调研

现在这方面的有对话系统，我记得我的文档里面提到了

# 4. Motivation

动机....讲真我也不知道要写什么，难不成要讲一个贼感人的故事什么我有一个抑郁症朋友阿巴阿巴

# 5. Functional Requirements

1. **User Interaction Interface**:
   
   - **Multiple Input Methods**: The platform should support various input methods, including keyboard typing and voice input, to cater to different user preferences.
   
   - System Layout
   
     : The interface should be easy to navigate and user-friendly, providing an intuitive user experience.
   
     - **Interactive Chat Interface**: Including the ability to input text and display chat conversations.
     - **Importing Chat History**: Users should be able to import historical chat data for reference and review.
     - **Report Downloading**: Feature to download chat history in PDF or Markdown format.
     - **Switching Models and Chats**: Users should be able to easily switch between different chat models.
2. **Mental Health Assessment**:

   - **Pre-set Assessment Questionnaires**: Including various mental health assessment tools, such as anxiety and depression self-assessment scales.
   - **Dialogue Analysis**: Analyzing the user's psychological state and personality traits through conversations.
   - **Personalized Reports**: Generating personalized mental health reports for users.
   - **Self-Improvement Suggestions**: Providing self-help improvement methods and suggestions based on the user's mental state.
   - **Emergency Contact Resources**: Offering contact resources and advice in emergency situations.

3. **Multilingual Support**:

   - Supporting multiple languages to meet the needs of users speaking different languages.

# 6. Non-Functional Requirements

1. **Performance Requirements**:
   - **Fast Response**: The system needs to respond quickly to user inputs and be able to actively send messages from the server to the client.
   - **Multi-user Support**: Ensure stability and performance when at least 5 people are using the system simultaneously.
2. **Scalability and Maintainability**:
   - **Easy to Expand and Maintain**: The system architecture should be designed with future scalability and maintainability in mind.
   - **Interface for Future Upgrades**: Reserve interfaces for future upgrades and feature additions.
3. **Security**:
   - **Data Encryption**: Encrypt user chats and inputs to protect user privacy.
4. **Compatibility**:
   - **Cross-platform Compatibility**: Should work well on various devices (such as mobile phones, tablets, computers).
   - **OS and Browser Compatibility**: Compatible with mainstream operating systems and browsers like Google Chrome.
5. **User Identity and Privacy Protection**:
   - **Anonymous Chat**: Provide anonymous chatting to protect user privacy.
   - **Chat Record Download**: Allow users to download chat records for continuing conversations later without cloud storage to ensure privacy.
6. **User Experience**:
   - **Interface and Responsiveness**: Ensure the interface is intuitive and responsive.
   - **Clear Error Messages and Guidance**: Provide clear error messages and helpful guidance.
7. **Legal and Ethical Compliance**:
   - **Compliance with Regulations and Ethics**: Comply with relevant mental health regulations and ethical standards.
   - **User Agreement and Privacy Policy**: Clearly define the user agreement and privacy policy.
8. **Reliability and Disaster Recovery**:
   - **High Reliability**: Ensure high system reliability to prevent data loss.
   - **Backup and Disaster Recovery**: Implement data backup and disaster recovery mechanisms.

# 7. Budget

1. **Server Costs**:
   - **Amazon Web Services (AWS) Server Costs**: We plan to rent an AWS cloud server for our service. According to AWS's pricing policy, the server usage is free for the first three months.
   - **Secondary Domain Name Cost**: We also plan to purchase a secondary domain name for the service. The cost for a month's secondary domain is approximately 20 RMB.

2. **OpenAI Token**:
   - We intend to use OpenAI's ChatGPT API as the underlying model for dialogues. Below is the official price list for the API:

     | Model                     | Input Cost          | Output Cost         |
     |---------------------------|---------------------|---------------------|
     | gpt-3.5-turbo-1106        | $0.0010 / 1K tokens | $0.0020 / 1K tokens |
     | gpt-3.5-turbo-instruct    | $0.0015 / 1K tokens | $0.0020 / 1K tokens |
     | gpt-4-0125-preview        | $0.01 / 1K tokens   | $0.03 / 1K tokens   |
     | gpt-4-1106-preview        | $0.01 / 1K tokens   | $0.03 / 1K tokens   |
     | gpt-4-1106-vision-preview | $0.01 / 1K tokens   | $0.03 / 1K tokens   |

   - During the testing phase, we plan to use `gpt-3.5-turbo-1106`. Based on our estimates, the cost per conversation round is about $0.05. During the development process, we do not expect to use more than $5 worth of API services.

# 8. Schedule