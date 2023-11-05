# HackNJIT2023 - Treasure Snap
Land Ahoy! Set sail across the seven seas to seek out buried treasures, with clues hidden in images ye share! Aye, capture all seven treasures, and may the wind be at yer back!
https://devpost.com/software/treasure-snap
## Technologies Used
- MongoDB & Atlas
- Streamlit
- Convolutional Neural Network

## Inspiration
Our inspiration for this project was geocaching, geoguessing, and treasure hunts in general.  We wanted the user to participate in challenges to find where another user took an image.  The goal was to emulate how pirates would hunt for treasure given obscure clues.  A player can choose to try and find the location of any image that is uploaded by any user.

## What it does
The application was built using the Streamlit framework and MongoDB (deployed using AWS) for data persistence.  A user can choose between many user-uploaded images, and try to find where exactly this image was taken.  To validate the attempts of the user, their uploads are compared with the chosen image in two ways–GPS location proximity and image similarity (using a CNN that calculates the cosine similarity between two images).  If the user successfully found the location of the image, they have found “the treasure”!  This achievement is saved to their profile which holds information about what other “treasures” they have found.

## How we built it
We built our application using GitHub, Streamlit, MongoDB, AWS, and Convolutional Neural Networks (CNNs). We utilized GitHub for storing our project with detailed pull requests and a project board to help us organize our tasks. Streamlit was utilized to host our project and develop our pages. We made use of Streamlit’s pages, forms, image uploads, buttons, and displaying content on our pages. MongoDB was used to host our users with their usernames, emails, passwords, and collected treasures. Additionally, it was also used for images along with their metadata that was used for our treasure hunt. MongoDB was hosted on AWS. Finally, Convolutional Neural Networks were utilized in our project to find the similarity in images sent by users compared to shown images. This allowed us to verify if the user had found the correct location combined with verifying with GPS coordinates to create a unique anti-cheat system.

## Challenges we ran into
A challenge we faced was our MongoDB cluster being quite limited in terms of storage size and performance.  Because we used the free tier (M0), storing too much image data severely slowed down the fetch speed.  It made us completely halt in development, more specifically for the most important feature of our application.

## Accomplishments that we're proud of
We were extremely proud of three main things.  Firstly, we have grown so much in our ability to use the Streamlit API.  We were introduced to the framework back in Girlhacks 2023, and our performance with it was decent at best.  This time around, we were able to use the API and accompanying packages so much more elegantly for session handling, DB configuration, and more.

Secondly, our task management in this hackathon was very organized.  We set up a GitHub repository and merged pull requests with meaningful commits.  We also avoided annoying and time-consuming merge conflicts in the process.  In this hackathon, we also set up Github issues and a KanBan board to organize our tasks and distribute them evenly among the team.

Finally, we were proud of implementing a creative validation system for comparing a user’s uploaded image with the challenge image.  Using the GPS location information in the EXIF data and implementing a CNN to compare the images with cosine similarity was a creative solution that followed the trending rise in AI/ML technologies.

## What we learned
We refined our use of Streamlit, resulting in a more elegant codebase.  We also learned more about the intricacies of MongoDB, allowing us to build a more robust data persistence layer.  Finally, we were able to implement ML into this project to compare the similarity of two images.

## What's next for Treasure Snap
The concept of Treasure Snap is awesome, but definitely needs some polishing.  We would like to deploy our app on Google Cloud so people can play.  With this deployment and public release, we would also need to upgrade to a better tier for our MongoDB cluster since many users will be uploading images.  We also had the idea of adding a DLC to our game, implementing Circle transaction services.  Finally, we would like to personalize the possible challenges for players by giving them image uploads based on their current GPS location.
