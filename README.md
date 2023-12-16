# PeerCode README

Welcome to PeerCode, a dynamic and collaborative coding platform! Whether you're a seasoned programmer or just starting your coding journey, PeerCode is designed to provide a comprehensive and immersive learning experience. Let's explore the key components that make PeerCode a unique platform for aspiring programmers and software engineers.

## User Service

The User Service is at the core of PeerCode, offering users a seamless and secure experience for managing their personal accounts. This service introduces essential features such as:

- **User Account Creation:** Easily set up your personal account by providing basic information like email and password.
- **Account Management:** Efficiently manage your account, edit personal details, and control your profile information.
- **User Authentication:** PEERCode prioritizes security with robust user authentication using Firebase, ensuring authorized access to user accounts.
- **User Authorization:** Admin rights, allowing specific users to create and manage questions, ensure a flexible and controlled environment.


## Question System

Explore coding challenges, receive guidance from Gen AI, and enhance your coding experience with the features offered by our Question System:

- **Gen AI Integration using ChatGPT:** Gen AI, our intelligent chatbot powered by Generative Artificial Intelligence, provides guidance, tips, and explanations to support your learning journey.
- **Question Filter:** Tailor your learning experience by effortlessly filtering questions based on different categories.
- **Update Question Status:** Track your progress dynamically as the system updates the question status on your dashboard.
- **Code Execution and Testing:** Run your code seamlessly, assess correctness with provided test cases, and benefit from iterative testing for practical learning.
- **Syntax Highlighting and Auto-Complete:** Elevate your coding experience with sophisticated syntax highlighting and auto-complete features.

## Matching System

The Matching System ensures a collaborative coding atmosphere, leveraging RabbitMQ messaging service for smooth collaboration among users. Key features include:

- **Match Two Users:** A sophisticated algorithm pairs users based on chosen difficulty levels, promoting effective teamwork and shared learning experiences.
- **Collaborative Chatbox:** Engage in real-time communication during coding sessions with an integrated chatbox, fostering a collaborative atmosphere.
- **Real-time Update:** Stay informed about your collaborator's progress with real-time updates on code runs and submissions.
- **Video Call Integration:** Enhance collaboration by offering video calling capabilities for a more immersive coding experience.

## History Service

The History Service plays a crucial role in capturing and presenting essential data to users, offering insights into their coding journey. Key components include:

- **Question Collection:** A comprehensive array of coding challenges totaling around 1-2k questions, sourced from platforms like LeetCode, providing a rich learning environment.
- **Question Status Collection:** Dynamically captures the status of user interactions with specific coding questions, offering a granular view of user engagement.
- **Submission Collection:** Captures crucial details with each code submission, providing insight into user performance, feedback, and code correctness.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/dunliang0513/peercode.git
   cd peercode
   ```

2. **Install Dependencies:**
   ```bash
   npm install
   ```

3. **Start PEERCode:**
   ```bash
   npm start
   ```

## License

PEERCode is released under the [MIT License](LICENSE).


## Acknowledgments

We extend our gratitude to the open-source community and contributors who have played a crucial role in shaping the PeerCode platform.

---

**Visit [PeerCode](http://peercode.net/) now to start your collaborative coding journey!**

Feel free to customize and expand upon this template to suit the specific details of your PEERCode platform.
