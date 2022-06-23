-I began to realize that I was not the only one who used meditation to assist with photography as I began to build the direction for the website. My initial plan is to have a museum type atmosphere due to some creative complimentary ideas but on early use the design did not work aesthetically. 

-I used my ideas to source if it was viable/feasible to complete using CSS code & built my wireframe this.

-Originally I tried to turn my radio button in an image slider on the home page which worked but after doing further research I realised this was not a popular user experience. Aslo gitpod discouraged the use of -webkitappearance which was the foundation of this function.

-Used Angela Delise online assistance in completing my Responsive CSS grid.

-Removed underline from text by using information from stack overflow text-decoration : none;

-It felt necessary to add the final blog page. The website was missing a key component to bring the vision of the website into balance of functionality.

-I solved alot of my positioning problems through using inspect software device to play with removing and adding various properties. I found that removing properties often came up with the best results


Used google & css to guide me through various steps from positioning to scaling

M initial wireframe plan didn't work, I couldn't find a colour balance to link the museum hero image in & the layout plan would not work with responsiveness to mobile. I see the radio button to flick through images but after reading it is not used I will likely drop that. Ideally when they click the image two arrows will come up either side to scroll but I think I need java script for that.

-Decided to keep it minimalist & professional with some features like hamburger menu to make completely minimalist header, apart from my logo.

-Changed the website text to match the logo

-I printed previously made an overlay with opacity. 5 to the navigation images on the home page but the overlay blocked from clicking, so instead of keeping the extremely long code, I added the writing to the image on a seperate application to make space on css. 80lines of code freed

-I found I wasn't been specific enough when i was trying to use thr dev tools to postion & shape my home page images. They were also targeting my logo image which gave me a fright but also explained a previous bug I couldn't solve so I restarted gitpod, lesson learned.

-Thank you to Speed Codez on YouTube for provoding code advice to change background image continously on intro page.

-Thanks to David Fitas on jot.form.com for the simple flat Contact for tips although edited to suit page

-I adapted the code for the hamburger from Erik Terwan of codepen.io but it was on the left side, so i found resolutions to change various aspects of the code by searching on stackoverflow!

-Major problem. I had the images balance in 2 comlumns & 10 rows, which actually started as 20 rows. I had each image place in name boxes of 20, from 1a to 10b. I then struggled to find the right balance as some images were slightly larger than others. When I chose all the images that fit inline & nicely beside eachother it worked. But I knew it was not sustainable & if I wanted to add new pictures the grid would have to be transformed.

-The images were too large & slowing down the web page & eating up unfortunate users monthly data in one click. I tried everything i could to stick with only using css & html, from using radio buttons to slide the images to shrinking the images unfortunately the website would not perform its main function well without the use of light box & a slight hint of Javascript.

-Discussed solution with my Mentor after he advised me that the images have to be reduced dramatically. They started out at approximately 5-8mb each, I reduced them to 1-2mb but this was far away from where it needed to be. My Mentor Felipe advised to check out gimp app platform for reducing image sizes dramatically(thumbnail size) & possibly use lightbox to link to the larger image.

-After a crash to the workspace, I figured I could download the complete repository from github & source the images direct from there. Saving enormous time & tedious work. But now to scale each image individually to a thumbnail, which is a step by step, generally tedious process. Which entails calculating the size of each image based on its role on the page. What size will the large image grow? How many images per page, therefore what size mb will each image be to not max out the page date etc

-Optimized images are essential for seo & user experience as per my discussions with my Mentor Felipe. I fixed the issue by shrinking the files using many applications from gimp to image-resizer etc.

-Fixed trouble with positioning of logo etc using justify-content & align-items: center;

-Thanks to Kasia I managed to fix the deploymemt issue when it did not recognise my css path. Kasia also helped resolve git pull issue after I edited readme.md via github repository, I was informed I had to pull it in to commit & accept it.

-As I could not find one background image that did not effect the visibility of the radio button query or forms. I had to remove 
the option of background translucency for the input form & add the < strong > attribute to the radio button query.

-hover over images in portfolio: I reduced the colour to start at 80%- then 100% when you hover, which is a much more positive user friendly experience than the opposite which it was previously.

-The introduction page works on all browzers but I was informed by a user that on firefox instead of transitioning it slides but is still effective. 

-Thanks to the tutor team for helping direct me to the resolution of my welcoming entry button issue due to the validator having an issue with an a tag wrapping a button.

-Contact form originally had translucency for the input area which I tried my best to make work but I couldn't find an image that would work with black or white colour text.
