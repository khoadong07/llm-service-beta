def llm_prompt(main_brand, content_input, template):
    """AI is creating summary for prompt

    Args:
        main_brand ([type]): [description]
        content ([type]): [description]
        template ([type]): [description]

    Raises:
        for: [description]

    Returns:
        [type]: [description]
    """
    return [
        {
            "role": "user",
            "content": "We are categorizing comments and posts related to the banking industry into appropriate topics and sub-topics. Based on the content of each comment or post, please assign a suitable label (topic) and sub-label (sub-topic) from the list below. Additionally, classify the content according to the newly defined fields.\n\n**List of Topics and Sub-Topics:**"
        },
        {
            "role": "user",
            "content": "We are categorizing comments and posts related to the banking industry into appropriate topics and sub-topics. Based on the content of each comment or post, please assign a suitable label (topic) and sub-label (sub-topic) from the list below. Additionally, classify the content according to the newly defined fields."
        },
        {
            "role": "user",
            "content": "**List of Topics and Sub-Topics:**\n\n1. **Products and Services**: The content relates to the financial utilities provided by banks. These products and services include accounts, loans, credit cards, insurance, and investment opportunities.\n    - **Credit cards**: Comments related to credit card benefits, rewards, interest rates, and issues.\n    - **Loan or Mortgage**: Discussions about personal loans, home loans, mortgage rates, loan applications, and experiences.\n    - **Savings account and Interest rates**: Topics about savings account features, interest rates, and account management.\n    - **Investment opportunities**: Comments on mutual funds, stocks, bonds, and other investment services.\n    - **Insurance products**: Discussions about life, health, auto insurance, and other coverage options."
        },
        {
            "role": "user",
            "content": "2. **Online Banking and Security**: The content relates to the online service that allows business/individual customers to conduct financial transactions over the internet. With online banking, you can access bank services 24/7 from everywhere with an internet connection. The content also relates to system, technology platform, process of online service.\n    - **Phishing scams or fraudulent activities**: Discussions about giving fake information or scams.\n    - **Password or login issues**: Users cannot log in due to a system error or the system denies logging in.\n    - **Online transaction security**: Content relevant to personal and financial information such as strong passwords, authenticators, and encryption.\n    - **Two-factor authentication**: Discussions about the second layer of security by requiring a second form of verification.\n    - **Mobile banking App**: Discussions about the app developed by the bank.\n    - **Information Leaking**: Complaints about customer information security.\n    - **Account Recovery and Assistance**: Discussions about support for account recovery.\n    - **Updates and Notifications**: Topics about new information or policies related to updating or changing service.\n    - **Transaction Failures or Delays**: Discussions about problems that may happen when conducting online transactions."
        },
        {
            "role": "user",
            "content": "3. **Branch and ATM Experiences**: The content relates to the physical interactions customers have with a bank's branch locations and ATMs. This includes the quality of service, accessibility, convenience, and overall customer experience when using in-person banking services and automated teller machines.\n    - **Waiting times or queues**: Comments regarding customer waiting times and queues when using services at branches or ATMs.\n    - **Friendly or unfriendly staff**: Discussions about the service attitude of bank staff: friendly/helpful, or not.\n    - **ATM fees or issues**: Comments on ATM services: fees, withdrawal/deposit process, technical errors.\n    - **Branch hours or locations**: Discussions about the opening hours and location of bank branches.\n    - **Accessibility and disability support**: Discussions about staff willingness to provide consultation."
        },
        {
            "role": "user",
            "content": "4. **Financial Advice and Education**: The content relates to managing money, investing, saving, and planning for the future.\n    - **Budgeting and saving tips**: Discussions about experience sharing for saving and creating a budget.\n    - **Investing and wealth management**: Topics related to investment portfolios, asset growth, and risk management.\n    - **Credit score and report**: Topics related to creditworthiness and personal information on the Vietnam Credit Information Center (CIC).\n    - **Financial planning and goals**: Topics about setting, organizing, and achieving financial goals."
        },
        {
            "role": "user",
            "content": "5. **Promotions and Offers**: This category encompasses various strategies and initiatives aimed at attracting and retaining customers through financial incentives and special deals. These can include discounts, loyalty programs, and other promotional tactics designed to boost sales and customer engagement.\n    - **Discounts or cashback offers**: Discussions about reducing the price or providing a cash return on purchases.\n    - **Limited-time promotions**: Discussions about special deals available for a short duration to encourage quick purchases.\n    - **Loyalty programs**: Discussions related to programs and incentives exclusively for members or priority customers (VIP).\n    - **Referral incentives**: Discussions about rewards given to customers who refer new clients to the business.\n    - **Special deals for students or seniors**: Discussions about discounts or special offers targeted specifically at students or senior citizens."
        },
        {
            "role": "user",
            "content": "6. **Technology and Innovation**: This topic covers advancements and applications of technology in the financial sector. It includes innovations such as financial technology (fintech), digital transformation, cybersecurity measures, and modern payment methods like mobile wallets and contactless payments, all of which aim to enhance efficiency and security.\n    - **Fintech and digital transformation**: Discussions about integrating digital technologies and strategies to optimize operations and enhance personalized experiences.\n    - **Cybersecurity and online safety**: Discussions related to attacks, damage, malware, viruses, hacking, data theft, and unauthorized access to networks, devices, programs, and data.\n    - **Mobile wallets and contactless payments**: Discussions about the go-to payment alternatives: mobile wallets, cards, and QR codes instead of cash."
        },
        {
            "role": "user",
            "content": "7. **Industry News and Updates**: This section focuses on the latest developments and trends within the industry. It includes changes in interest rates, economic forecasts, significant mergers and acquisitions, new product introductions, and updates to regulatory frameworks that impact the industry.\n    - **Interest rate changes**: Topics on changes in borrowing costs, typically set by central banks, impacting loans and savings.\n    - **Economic trends and forecasts**: Discussions about analyzing and predicting the overall economic environment and its future direction.\n    - **Mergers and acquisitions**: Discussions about the process where companies combine (merger) or one company purchases another (acquisition).\n    - **New product launches**: Regarding the launch of new products into the market.\n    - **Regulatory changes**: Discussions about changes or revisions to laws and regulations impacting the industry."
        },
        {
            "role": "user",
            "content": "8. **Corporation**: This topic pertains to internal and external corporate matters. It includes information about company leadership, organizational campaigns and events, awards received, shareholder meetings, overall business performance, and corporate mergers and acquisitions.\n    - **BOD / Leaders**: Discussions about the Board of Directors and key leaders in the organization.\n    - **Campaign / Event (CSR, Minigame, Livestream, ...)**: Discussions about campaigns and events, community activities hosted/contributed by banks.\n    - **Awards**: Discussions about recognition or honors given to the corporation for achievements or excellence in different areas.\n    - **Shareholders meeting**: About meetings where shareholders discuss and vote on company matters.\n    - **Business performance**: Analysis and reporting of the company's financial and operational performance.\n    - **Mergers and acquisitions**: The process where companies combine (merger) or one company purchases another (acquisition)."
        },
        {
            "role": "user",
            "content": "9. **Customer Insights**: This area involves understanding and addressing customer experiences and feedback. It includes resolving customer complaints, gathering feedback on products and services, suggestions for improvements, comparative analyses with competitors, interactions between customers and bank staff, and details on fees or charges associated with the company’s offerings.\n    - **Resolving issues or complaints**: Addressing and solving customer problems and grievances.\n    - **Feedback about products or services**: Customer opinions and reviews about the company's offerings.\n    - **Suggestions for improvement**: Recommendations from customers on how the company can enhance its products or services.\n    - **Comparisons with other banks**: Analysis of how the company's services and products stack up against competitors.\n    - **Interactions with bank staff**: Customer experiences and engagements with the bank's employees.\n    - **Fees or charges**: Information about various costs associated with the company's products and services."
        },
        {
            "role": "user",
            "content": "Additional Fields Definitions:**\n\n- sentiment: The sentiment towards the main brand, with possible values: POSITIVE, NEGATIVE, NEUTRAL, MIXED\n- severity: An assessment of the severity of the sentiment, possible values: LOW, MEDIUM, HIGH, VERY HIGH, CRITICAL\n- emotion: Evaluation of the emotion expressed towards the main brand, possible values: Anger, Disgust, Fear, Happiness, Sadness, Surprise, Interest, Joy\n- polarity: The degree of emotion expressed in relation to the main brand, ranging from -1 to 1\n- intensity: The intensity of the emotion expressed towards the main brand, possible values: LOW, MEDIUM, HIGH\n- category: Prediction of the field to which the text belongs\n- industry: Prediction of the industry to which the text belongs\n- subject: The person or entity mentioned in the text, empty if none\n- product_type: The type of product mentioned in the text, empty if none\n- angle: The perspective mentioned in the text, empty if none\n- entity_recognition: A list of objects containing entities mentioned in the text, each with:\n  - type: The type of entity (e.g., Organization, Product)\n  - value: The entity value mentioned in the text\n- intent: The intent expressed in the text, one or more of the following values: Help, Search, Booking, Payment, Feedback, Complaint\n- purpose: The purpose stated in the text, empty if none\n- tone: The tone(s) expressed in the text, possible values: Friendly, Informal, Positive, Excited\n- audience: The audience mentioned in the text, empty if none\n- mention_mainbrand: true if the main brand exists, false otherwise\n- context: A list of objects containing words, phrases, or sentences related to the main brand, each with:\n  - sentiment: The sentiment of the keyword, which must match the sentiment of the main text (POSITIVE, NEGATIVE, MIXED)\n  - value: The word, phrase, or sentence that clearly expresses the sentiment\n- explanation: A brief summary or statement reflecting the sentiment towards the main brand.\n- spam: Determine if the text being analyzed is spam, the result is a string with the value 'YES' or 'NO'\n- advertisement: Determine if the text being analyzed is advertising a product or service, the result is a string with the value 'YES' or 'NO'\n- opinion_expressed: Determine if the text being analyzed has opinion express or not, the result is a string with the value 'YES' or 'NO'\n- emotional_tone: Determine if the text being analyzed has emotional tone or not, the result is a string with the value 'YES' or 'NO'\n- feedback_provided: Determine if the text being analyzed has provide feedback or not, the result is a string with the value 'YES' or 'NO'\n- insight_provided: Determine if the text being analyzed has provide insight or not, the result is a string with the value 'YES' or 'NO'\n\nPlease apply this rule to all comments and posts to ensure accurate and consistent categorization."
        },
        {
            "role": "user",
            "content": "Constrain subtopics predictions to be within the topic as described"
        },
        {
            "role": "user",
            "content": "The values True/False are always replaced by true/false to conform to the JSON format",
        },
        {
            "role": "user",
            "content": f"The result always returns in JSON format with all fields as shown in the template: {template}"
        },
        {
            "role": "user",
            "content": f"content: \"{content_input}\"\nmain_brand: [\"{main_brand}\"]"
        },
        {
            "role": "user",
            "content": "Automatically format JSON when exporting the result."
        },
        {
            "role": "user",
            "content": f"Ensure that the output is always a JSON. In case of failure, return {template}."
        },
        {
            "role": "user",
            "content": "Please format the result for me, outputting only JSON data, discarding any non-JSON data"
        },
        {
            "role": "user",
            "content": "Skip any notes or additional explanations after the JSON, ensuring that the output is always a correctly formatted JSON"
        }
    ]


def contex_prompt(main_brand, content_input):
    prompt = [
        {
            "role": "user",
            "content": "Bạn được yêu cầu phân tích dữ liệu từ việc theo dõi mạng xã hội trong ngành ngân hàng. Dưới đây là các bước để phân tích dữ liệu từ social listening. We are categorizing comments and posts related to the banking industry into appropriate topics and sub-topics. Based on the content of each comment or post, please assign a suitable label (topic) and sub-label (sub-topic) from the list below. Additionally, classify the content according to the newly defined fields.\n\n**List of Topics and Sub-Topics:**"
        },
        {
            "role": "user",
            "content": "We are categorizing comments and posts related to the banking industry into appropriate topics and sub-topics. Based on the content of each comment or post, please assign a suitable label (topic) and sub-label (sub-topic) from the list below. Additionally, classify the content according to the newly defined fields."
        },
        {
            "role": "user",
            "content": "**List of Topics and Sub-Topics:**\n\n1. **Products and Services**: The content relates to the financial utilities provided by banks. These products and services include accounts, loans, credit cards, insurance, and investment opportunities.\n    - **Credit cards**: Comments related to credit card benefits, rewards, interest rates, and issues.\n    - **Loan or Mortgage**: Discussions about personal loans, home loans, mortgage rates, loan applications, and experiences.\n    - **Savings account and Interest rates**: Topics about savings account features, interest rates, and account management.\n    - **Investment opportunities**: Comments on mutual funds, stocks, bonds, and other investment services.\n    - **Insurance products**: Discussions about life, health, auto insurance, and other coverage options."
        },
        {
            "role": "user",
            "content": "2. **Online Banking and Security**: The content relates to the online service that allows business/individual customers to conduct financial transactions over the internet. With online banking, you can access bank services 24/7 from everywhere with an internet connection. The content also relates to system, technology platform, process of online service.\n    - **Phishing scams or fraudulent activities**: Discussions about giving fake information or scams.\n    - **Password or login issues**: Users cannot log in due to a system error or the system denies logging in.\n    - **Online transaction security**: Content relevant to personal and financial information such as strong passwords, authenticators, and encryption.\n    - **Two-factor authentication**: Discussions about the second layer of security by requiring a second form of verification.\n    - **Mobile banking App**: Discussions about the app developed by the bank.\n    - **Information Leaking**: Complaints about customer information security.\n    - **Account Recovery and Assistance**: Discussions about support for account recovery.\n    - **Updates and Notifications**: Topics about new information or policies related to updating or changing service.\n    - **Transaction Failures or Delays**: Discussions about problems that may happen when conducting online transactions."
        },
        {
            "role": "user",
            "content": "3. **Branch and ATM Experiences**: The content relates to the physical interactions customers have with a bank's branch locations and ATMs. This includes the quality of service, accessibility, convenience, and overall customer experience when using in-person banking services and automated teller machines.\n    - **Waiting times or queues**: Comments regarding customer waiting times and queues when using services at branches or ATMs.\n    - **Friendly or unfriendly staff**: Discussions about the service attitude of bank staff: friendly/helpful, or not.\n    - **ATM fees or issues**: Comments on ATM services: fees, withdrawal/deposit process, technical errors.\n    - **Branch hours or locations**: Discussions about the opening hours and location of bank branches.\n    - **Accessibility and disability support**: Discussions about staff willingness to provide consultation."
        },
        {
            "role": "user",
            "content": "4. **Financial Advice and Education**: The content relates to managing money, investing, saving, and planning for the future.\n    - **Budgeting and saving tips**: Discussions about experience sharing for saving and creating a budget.\n    - **Investing and wealth management**: Topics related to investment portfolios, asset growth, and risk management.\n    - **Credit score and report**: Topics related to creditworthiness and personal information on the Vietnam Credit Information Center (CIC).\n    - **Financial planning and goals**: Topics about setting, organizing, and achieving financial goals."
        },
        {
            "role": "user",
            "content": "5. **Promotions and Offers**: This category encompasses various strategies and initiatives aimed at attracting and retaining customers through financial incentives and special deals. These can include discounts, loyalty programs, and other promotional tactics designed to boost sales and customer engagement.\n    - **Discounts or cashback offers**: Discussions about reducing the price or providing a cash return on purchases.\n    - **Limited-time promotions**: Discussions about special deals available for a short duration to encourage quick purchases.\n    - **Loyalty programs**: Discussions related to programs and incentives exclusively for members or priority customers (VIP).\n    - **Referral incentives**: Discussions about rewards given to customers who refer new clients to the business.\n    - **Special deals for students or seniors**: Discussions about discounts or special offers targeted specifically at students or senior citizens."
        },
        {
            "role": "user",
            "content": "6. **Technology and Innovation**: This topic covers advancements and applications of technology in the financial sector. It includes innovations such as financial technology (fintech), digital transformation, cybersecurity measures, and modern payment methods like mobile wallets and contactless payments, all of which aim to enhance efficiency and security.\n    - **Fintech and digital transformation**: Discussions about integrating digital technologies and strategies to optimize operations and enhance personalized experiences.\n    - **Cybersecurity and online safety**: Discussions related to attacks, damage, malware, viruses, hacking, data theft, and unauthorized access to networks, devices, programs, and data.\n    - **Mobile wallets and contactless payments**: Discussions about the go-to payment alternatives: mobile wallets, cards, and QR codes instead of cash."
        },
        {
            "role": "user",
            "content": "7. **Industry News and Updates**: This section focuses on the latest developments and trends within the industry. It includes changes in interest rates, economic forecasts, significant mergers and acquisitions, new product introductions, and updates to regulatory frameworks that impact the industry.\n    - **Interest rate changes**: Topics on changes in borrowing costs, typically set by central banks, impacting loans and savings.\n    - **Economic trends and forecasts**: Discussions about analyzing and predicting the overall economic environment and its future direction.\n    - **Mergers and acquisitions**: Discussions about the process where companies combine (merger) or one company purchases another (acquisition).\n    - **New product launches**: Regarding the launch of new products into the market.\n    - **Regulatory changes**: Discussions about changes or revisions to laws and regulations impacting the industry."
        },
        {
            "role": "user",
            "content": "8. **Corporation**: This topic pertains to internal and external corporate matters. It includes information about company leadership, organizational campaigns and events, awards received, shareholder meetings, overall business performance, and corporate mergers and acquisitions.\n    - **BOD / Leaders**: Discussions about the Board of Directors and key leaders in the organization.\n    - **Campaign / Event (CSR, Minigame, Livestream, ...)**: Discussions about campaigns and events, community activities hosted/contributed by banks.\n    - **Awards**: Discussions about recognition or honors given to the corporation for achievements or excellence in different areas.\n    - **Shareholders meeting**: About meetings where shareholders discuss and vote on company matters.\n    - **Business performance**: Analysis and reporting of the company's financial and operational performance.\n    - **Mergers and acquisitions**: The process where companies combine (merger) or one company purchases another (acquisition)."
        },
        {
            "role": "user",
            "content": "9. **Customer Insights**: This area involves understanding and addressing customer experiences and feedback. It includes resolving customer complaints, gathering feedback on products and services, suggestions for improvements, comparative analyses with competitors, interactions between customers and bank staff, and details on fees or charges associated with the company’s offerings.\n    - **Resolving issues or complaints**: Addressing and solving customer problems and grievances.\n    - **Feedback about products or services**: Customer opinions and reviews about the company's offerings.\n    - **Suggestions for improvement**: Recommendations from customers on how the company can enhance its products or services.\n    - **Comparisons with other banks**: Analysis of how the company's services and products stack up against competitors.\n    - **Interactions with bank staff**: Customer experiences and engagements with the bank's employees.\n    - **Fees or charges**: Information about various costs associated with the company's products and services."
        },
        {
            "role": "user",
            "content": "Bạn được yêu cầu phân tích dữ liệu từ việc theo dõi mạng xã hội trong ngành ngân hàng. Dưới đây là các bước để phân tích dữ liệu từ social listening:\n\n1. **Thu thập dữ liệu:**\n   - Theo dõi các bài đăng, bình luận và thảo luận trên các nền tảng mạng xã hội như Facebook, Twitter, LinkedIn, và Reddit liên quan đến ngành ngân hàng.\n   - Thu thập các dữ liệu như nội dung bài đăng, người đăng, thời gian đăng, số lượt tương tác, và các từ khóa quan trọng.\n\n2. **Phân loại chủ đề:**\n   - Xác định chủ đề chính của từng bài đăng dựa trên nội dung và từ khóa liên quan.\n   - Phân loại các chủ đề theo danh sách đã cung cấp như sản phẩm và dịch vụ, trải nghiệm ngân hàng trực tuyến, trải nghiệm tại chi nhánh, tư vấn tài chính, và các chương trình khuyến mãi.\n\n3. **Đánh giá sắc thái:**\n   - Phân tích sắc thái của mỗi bài đăng và bình luận để xác định tình hình cảm xúc chung của cộng đồng mạng đối với ngân hàng.\n   - Đánh giá sắc thái dựa trên các dấu hiệu như từ ngữ tích cực, tiêu cực, hoặc trung lập.\n\n4. **Tổng hợp và báo cáo:**\n   - Tổng hợp kết quả phân tích để tạo ra báo cáo tổng quan về tình hình trên mạng xã hội liên quan đến ngân hàng.\n   - Cung cấp thông tin chi tiết về các chủ đề phổ biến, sắc thái chung, và xu hướng đang diễn ra trong cộng đồng mạng.\n\n5. **Đề xuất giải pháp:**\n   - Dựa trên kết quả phân tích, đề xuất các giải pháp hoặc cải tiến để cải thiện hình ảnh và dịch vụ của ngân hàng trên mạng xã hội.",
            "prompt_completion": {
                "post": {
                    "sentiment": "",
                    "topic": "",
                    "subtopic": ""
                },
                "comment": [
                    {
                        "id": "",
                        "sentiment": "",
                        "keywords": []
                    }
                ]
            }
        }

    ]

    sentiment = {
        "role":"user",
        "content": ""
    }

    sample_input = {
        "content": "NHà tôi có vay bên ngân hàng msb chi nhánh quế võ bắc ninh 1 khoản vay. Hiện giờ nhà tôi muốn tất "
                   "toán khoản vay nhưng bên ngân hàng bảo chờ xét duyệt ??? Vậy tiền lãi phát sinh trong lúc chờ ai "
                   "thanh toán ?? Bên ngân hàng cũng không nói rõ phải chờ đến bao giờ. Nhà tôi cứ phải chờ thôi à ?",
        "id": "123",
        "comment": [
            {
                "id": "1419474048711328_1419476458711087",
                "content": "Cụ nhà nó lúc vay thì nịnh khach lên nịnh khách xuống. Xong giờ dở trò bố đời mẹ thiên "
                           "hạ. Muốn trả nợ cũng khó :))"
            },
            {
                "id": "1419474048711328_1419477412044325",
                "content": "Định mệnh! Lúc đi vay phải nịnh nó,giờ muốn trả phải quỳ lạy nó nữa 😅😅😅"
            },
            {
                "id": "1419474048711328_1419476478711085",
                "content": "Đỏ MSB ạ 🤣🤣🤣"
            },
            {
                "id": "1419474048711328_1419477158711017",
                "content": "Gửi số đt của nó lên đây bác."
            },
            {
                "id": "1419474048711328_1419477212044345",
                "content": "Hỏi được tên nhân viên  ,địa chỉ nơi làm việc  mxh phát triển mình làm đúng theo trình tự "
                           "thì đảm bảo ngân hàng đấy ngày hôm sau phải xin lỗi bác :))"
            },
            {
                "id": "1419474048711328_1419477708710962",
                "content": "Lên tận chi nhánh đó. Gặp thẳng giám đốc. Nói chuyện cho ra nhẽ. Rồi cho nó đọc tin nhắn "
                           "nhân viên nc với khách hàng. 3 mặt 1 lời luôn"
            },
            {
                "id": "1419474048711328_1419477502044316",
                "content": "Lên thẳng gặp GĐ chi nhánh, ko thì cho cái đơn lên hội sở hoặc VP miền. Sợ xoắn ngay"
            }
        ]
    }

    {
        "role": "user",
        "content": "Bạn được yêu cầu phân loại chủ đề và đánh giá sắc thái của bài đăng và các bình luận liên quan "
                   "đến ngành ngân hàng. Dưới đây là danh sách các chủ đề và sắc thái:\n\n**Chủ đề và Phân loại Chủ "
                   "đề:**\n\n1. **Products and Services**: Nội dung liên quan đến các sản phẩm và dịch vụ tài chính "
                   "do ngân hàng cung cấp như tài khoản, khoản vay, thẻ tín dụng, bảo hiểm, và cơ hội đầu tư.\n   - "
                   "**Credit cards**\n   - **Loan or Mortgage**\n   - **Savings account and Interest rates**\n   - "
                   "**Investment opportunities**\n   - **Insurance products**\n\n2. **Online Banking and Security**: "
                   "Nội dung liên quan đến dịch vụ ngân hàng trực tuyến và bảo mật.\n   - **Phishing scams or "
                   "fraudulent activities**\n   - **Password or login issues**\n   - **Online transaction "
                   "security**\n   - **Two-factor authentication**\n   - **Mobile banking App**\n   - **Information "
                   "Leaking**\n   - **Account Recovery and Assistance**\n   - **Updates and Notifications**\n   - "
                   "**Transaction Failures or Delays**\n\n3. **Branch and ATM Experiences**: Nội dung liên quan đến "
                   "trải nghiệm tại các chi nhánh và máy ATM.\n   - **Waiting times or queues**\n   - **Friendly or "
                   "unfriendly staff**\n   - **ATM fees or issues**\n   - **Branch hours or locations**\n   - "
                   "**Accessibility and disability support**\n\n4. **Financial Advice and Education**: Nội dung liên "
                   "quan đến quản lý tài chính, đầu tư, tiết kiệm và lập kế hoạch tài chính.\n   - **Budgeting and "
                   "saving tips**\n   - **Investing and wealth management**\n   - **Credit score and report**\n   - "
                   "**Financial planning and goals**\n\n5. **Promotions and Offers**: Các chiến lược và sáng kiến để "
                   "thu hút và giữ chân khách hàng thông qua các ưu đãi tài chính và các chương trình khuyến mãi.\n   "
                   "- **Discounts or cashback offers**\n   - **Limited-time promotions**\n   - **Loyalty programs**\n "
                   "  - **Referral incentives**\n   - **Special deals for students or seniors**\n\n**Sắc thái:**\n- "
                   "POSITIVE\n- NEGATIVE\n- NEUTRAL\n- MIXED\n\n**Ví dụ Input:**\n\n```json\n{\n    \"post\": \"NHà "
                   "tôi có vay bên ngân hàng msb chi nhánh quế võ bắc ninh 1 khoản vay. Hiện giờ nhà tôi muốn tất "
                   "toán khoản vay nhưng bên ngân hàng bảo chờ xét duyệt ??? Vậy tiền lãi phát sinh trong lúc chờ ai "
                   "thanh toán ?? Bên ngân hàng cũng không nói rõ phải chờ đến bao giờ. Nhà tôi cứ phải chờ thôi à "
                   "?\",\n    \"comment\": [\n        {\n            \"id\": \"1419474048711328_1419476458711087\","
                   "\n            \"content\": \"Cụ nhà nó lúc vay thì nịnh khach lên nịnh khách xuống. Xong giờ dở "
                   "trò bố đời mẹ thiên hạ. Muốn trả nợ cũng khó :))\"\n        },\n        {\n            \"id\": "
                   "\"1419474048711328_1419477412044325\",\n            \"content\": \"Định mệnh! Lúc đi vay phải "
                   "nịnh nó,giờ muốn trả phải quỳ lạy nó nữa 😅😅😅\"\n        },\n        {\n            \"id\": "
                   "\"1419474048711328_1419476478711085\",\n            \"content\": \"Đỏ MSB ạ 🤣🤣🤣\"\n        },"
                   "\n        {\n            \"id\": \"1419474048711328_1419477158711017\",\n            \"content\": "
                   "\"Gửi số đt của nó lên đây bác.\"\n        },\n        {\n            \"id\": "
                   "\"1419474048711328_1419477212044345\",\n            \"content\": \"Hỏi được tên nhân viên ,"
                   "địa chỉ nơi làm việc mxh phát triển mình làm đúng theo trình tự thì đảm bảo ngân hàng đấy ngày "
                   "hôm sau phải xin lỗi bác :))\"\n        },\n        {\n            \"id\": "
                   "\"1419474048711328_1419477708710962\",\n            \"content\": \"Lên tận chi nhánh đó. Gặp "
                   "thẳng giám đốc. Nói chuyện cho ra nhẽ. Rồi cho nó đọc tin nhắn nhân viên nc với khách hàng. 3 mặt "
                   "1 lời luôn\"\n        },\n        {\n            \"id\": \"1419474048711328_1419477502044316\","
                   "\n            \"content\": \"Lên thẳng gặp GĐ chi nhánh, ko thì cho cái đơn lên hội sở hoặc VP "
                   "miền. Sợ xoắn ngay\"\n        }\n    ]\n}\n```\n\n**Yêu cầu:**\n\n1. **Phân loại Chủ đề của bài "
                   "đăng**:\n   - Xác định chủ đề chính của bài đăng dựa trên nội dung và từ khóa liên quan.\n\n2. "
                   "**Đánh giá Sắc thái của bài đăng**:\n   - Đánh giá sắc thái của bài đăng (POSITIVE, NEGATIVE, "
                   "NEUTRAL, MIXED).\n\n3. **Phân loại Chủ đề và Đánh giá Sắc thái của các bình luận đi kèm**:\n   - "
                   "Đối với mỗi bình luận, xác định chủ đề và đánh giá sắc thái trong ngữ cảnh của bài đăng.\n   - "
                   "Trích xuất các từ khóa thể hiện sắc thái đi kèm.\n\n**Output Mẫu:**\n\n- **Bài đăng**:\n  - Chủ "
                   "đề: Loan or Mortgage\n  - Sắc thái: NEGATIVE\n\n- **Bình luận**:\n  - ID: "
                   "1419474048711328_1419476458711087\n    - Chủ đề: Loan or Mortgage\n    - Sắc thái: NEGATIVE\n    "
                   "- Từ khóa sắc thái: \"nịnh khach\", \"dở trò\", \"khó\"\n\n  - ID: "
                   "1419474048711328_1419477412044325\n    - Chủ đề: Loan or Mortgage\n    - Sắc thái: NEGATIVE\n    "
                   "- Từ khóa sắc thái: \"nịnh\", \"quỳ lạy\"\n\n  - ID: 1419474048711328_1419476478711085\n    - Chủ "
                   "đề: Loan or Mortgage\n    - Sắc thái: NEUTRAL\n    - Từ khóa sắc thái: \"Đỏ MSB\"\n\n  - ID: "
                   "1419474048711328_1419477158711017\n    - Chủ đề: Loan or Mortgage\n    - Sắc thái: NEUTRAL\n    - "
                   "Từ khóa sắc thái: N/A\n\n  - ID: 1419474048711328_1419477212044345\n    - Chủ đề: Loan or "
                   "Mortgage\n    - Sắc thái: MIXED\n    - Từ khóa sắc thái: \"xin lỗi\"\n\n  - ID: "
                   "1419474048711328_1419477708710962\n    - Chủ đề: Loan or Mortgage\n    - Sắc thái: NEUTRAL\n    - "
                   "Từ khóa sắc thái: N/A\n\n  - ID: 1419474048711328_1419477502044316\n    - Chủ đề: Loan or "
                   "Mortgage\n    - Sắc thái: NEUTRAL\n    - Từ khóa sắc thái: N/A\n\nVới prompt này, bạn có thể nhận "
                   "định chủ đề và sắc thái của các bài đăng và bình luận một cách rõ ràng và có cấu trúc."
    }


result = {
    "post": {
        "sentiment": "",
        "topic": ""
        "subtopic": ""
    },
    "comment": [
        {
            "id": "",
         "sentiment": "",
         "keywords": []
        },
        ...
    ]
}