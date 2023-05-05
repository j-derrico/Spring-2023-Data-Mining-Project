# Non-English Film Engagement on IMDb

Marcus Almanza

Yoshie Bell-Souder

Emily Carpenter

Janet Matthews-Derrico


## Description

As media is increasingly globalized, the success in recent years of films like *Parasite* (Bong, 2019) and *All Quiet on the Western Front* (Berger, 2022) demonstrate the widespread potential for non-English language films in the English-speaking market.  First launched in 1990, today the Internet Movie Database (IMDb) is a comprehensive, U.S.-based online database of information primarily pertaining to films and television shows.  Its reviews and ratings systems offer a way to measure user engagement, which can represent a mode of success that is different from more traditional measures such as ticket sales and awards.
 
With this project, we aimed to explore user engagement with non-English language films listed on IMDb.  We were most interested in looking for interesting patterns in the number of user votes—that is, the number of distinct user profiles that had voted on a film rating between 0 and 10—as well as the film ratings themselves.  To that end, we developed a set of specific questions around the number of votes, ratings, film language, release year, and genre that we hoped could be answered by the data.

We began by preprocessing and integrating several different datasets available from IMDb.  From there, we developed tools to fill in missing data primarily centered around the film language—an integral part of our research questions.  We then employed data mining tools in an effort to determine whether there are certain that lead to greater user engagement on IMDb.  We found that while there is overall a heavy disparity between English and non-English films, the language of the film itself as well as the genre may have a sizable effect on user engagement.

## Questions

We developed six key research questions for this project:
- Do non-English films have fewer reviews and ratings, regardless of their average rating?
- Do international films have higher ratings due to fewer view counts?
- Do certain languages do better when it comes to ratings/reviews overall? 
- Do certain genres of non-English films do better?  How does this compare to English film genres?
- Which films are “underrated gems,” those that have high ratings, but relatively low view counts? 
- Do certain directors have more user-engagement than others, and does the rate of engagement vary based on the language?

## Findings

### Do non-English films have fewer reviews and ratings, regardless of their average rating?  Do international films have higher ratings due to fewer view counts?

Running a T-test, the non-English group of movies has significantly fewer votes (reviews). On average the non-English films had 7,131 fewer votes than English films (t value = 46.068, p < 0.001). This assumes that variance is roughly equivalent, we would say non-English films have fewer reviews, but the rating is not much affected by the fewer reviews. 

<img width="297" alt="Screen Shot 2023-05-04 at 12 39 40 PM" src="https://user-images.githubusercontent.com/105665462/236298320-09d84832-48ab-4850-bb7f-6d7a63f0dbb4.png">
Figure 1: Scatterplot Between the Number of Votes and the Number of Rating
Blue: English films Red: non-English films
<br> </br>

We again examined the p test,  and found that non-English movie ratings on average (about 6.2) are higher than the average rating for English movies (6.0798). Looking at a standard error of 0.005, T value of 23.565, and P value less than 0.001. It is significant, but may not be practically significant.


### Do certain languages do better when it comes to ratings/reviews overall? 

In looking at the number of films for each language (excluding English), the top five were Spanish, French, German, Italian, and Japanese.  Of these, only Spanish and French are among the top 10 most spoken languages in the world as of 2022 according to Ethnologue.  The top five languages ranked by the number of user votes were French, Hindi, Italian, Spanish, and Japanese.  This aligns slightly more with the most spoken languages in the world in that Hindi is number three after English and Mandarin Chinese.  However, our results overall suggest that the number of user votes is not strongly tied to the number of global speakers of the film’s language.

We then looked at individual languages that had at least 1,000 movies to see if any language seemed to have a significantly higher average rating. We found that Bengali had an average rating of about 6.89 among films that contained at least 100 votes.  The standard deviation among average rating is 1.267.  This information taken in conjunction with the overall dispersal of data suggests that the high rating among Bengali films is not simply a result of one or two films skewing the average.  There are 272.7 million Bengali speakers around the world, making it the 7th most spoken language globally.


### Do certain genres of non-English films do better?  How does this compare to English film genres?

In examining the user engagement with regards to genre, we found that the most generally popular genre in non-English language films is Drama.  We are defining popularity here by the total number of user votes rather than by rating–a high user engagement on a film with a lower rating can still be interpreted as a measure of success.  The non-English popularity of the Drama genre is in contrast to English language films, in which the most popular genre was Action/Adventure/Sci-Fi.  Although the genre composition for the top fifteen languages (‘top’ is again defined by the total number of user votes) varied from language to language, Drama was a notable percentage for all but one. 

<img width="303" alt="Screen Shot 2023-05-04 at 12 43 04 PM" src="https://user-images.githubusercontent.com/105665462/236299005-d77a218a-575c-450f-934c-24d59582210d.png"> 
Figure 2: Number of films in each language by genre
<br> </br>

We identified Crime/Drama/Mystery as the genre with the highest average of user votes per film.  This genre accounts for only 0.004% of non-English films and 0.47% of films overall.  Of all Crime/Drama/Mystery films, over one quarter were released within the past ten years which may explain the popularity of a genre that makes up a relatively small percentage of films in the dataset.  In contrast, the genre with the highest average votes per English language film was Action/Adventure/Sci-Fi. 


### Which films are “underrated gems,” those that have high ratings, but relatively low view counts?

We sought to identify “underrated gems,” films with relatively few vote counts despite a comparatively high average ratings. we explored the relationship between number of votes and the average rating of films using a scatter plot, which slopes from the densest data point area on the left to the highest ratings on the right. Using a regression model with 2.5 upper and lower standard deviation to focus on the underrated gems, we were able to find about 400 films as underrated gems with about 1% confidence. 

<img width="300" alt="Screen Shot 2023-05-04 at 12 49 08 PM" src="https://user-images.githubusercontent.com/105665462/236300332-64ac56c1-4c6d-4847-b2ff-82e1caab1266.png">
Figure 3: Linear regression Between the Number of Votes and the Average Rating with 2.5 standard deviation.
<br> </br>

It can be hard to conclude with certainty that recent movies or movies with a relatively low number of view counts will continue to have such high ratings. If we expand this search and look at movies with an average rating of 8.0 or higher with more than 15,000 votes, but not more than 30,000 votes, we see another picture emerge when it comes to underrated gems. In the scatterplot below, we see about an even number of red and blue, red being films before 1979 and blue being films after 1979. This is surprising because the number of films made in the 2010s alone outnumbers the total number of films made before 1980. This would imply that the real underrated gems are actually older films. 

<img width="309" alt="Screen Shot 2023-05-04 at 12 51 35 PM" src="https://user-images.githubusercontent.com/105665462/236300852-f5af3eba-e8ae-42f7-820b-b6b75aa89fda.png">
Figure 4: Underrated gems
<br> </br>

Of the 74 films that fit the criteria above, only 21 of them are English-language, despite English films making up nearly half of the films on IMDb. This would indicate that a majority of underrated gems, those that are under-watched for their quality, are mostly older foreign films. A further measure of the quality of these films is the decennial poll produced by Sight & Sound, a magazine published by the British Film Institute, of the 250 Greatest Films of All Time. This list was last updated in 2022 and fifteen of the films we’ve determined are underrated gems also appear on this list. Nine of those are featured in both the Sight & Sound Top 100 and on our list:
- *Man with a Movie Camera* (Vertov, 1929), a Russian documentary ranked 9th with a rating of 8.4 
- *Late Spring* (Ozu, 1949), a Japanese movie ranked 22nd with a rating of 8.2 
- *Ali: Fear Eats the Soul* (Fassbinder, 1974), a German movie ranked 53rd with a rating of 8.0 
- *Sansho the Bailiff* (Mizoguchi, 1954), a Japanese movie ranked 76th with a rating of 8.4 
- *A Matter of Life and Death* (Powell & Pressburger, 1946), an English film ranked 83rd with a rating of 8.0
- *The Leopard* (Visconti, 1963), an Italian film ranked 91st with a rating of 8.0
- *Ugetsu* (Mizoguchi, 1953), a Japanese film ranked 92nd with a rating of 8.2
- *Yi Yi* (Yang, 2000), a Mandarin film ranked 94th with a rating of 8.1 
- *A Man Escaped* (Bresson, 1956), a French film ranked 95th with a rating of 8.2 

### Do certain directors have more user-engagement than others, and does the rate of engagement vary based on the language?

Directors like James Cameron and Christopher Nolan are capable of amassing billions of dollars at the global box office throughout their careers. Steven Speilberg alone has managed to gross over $10 billion worldwide with hits like *Jaws* (1975), *Raiders of the Lost Ark* (1981), *Jurassic Park* (1993), *E.T.* (1982), and *Saving Private Ryan* (1998). Movie ratings for Spielberg’s films alone account for 1.65% of all ratings for English films. In the same vein, Christopher Nolan’s ratings are 1.74% of all English film ratings. Only five other English-language directors cross this 1% threshold: Quentin Tarantino, Martin Scorsese, Ridley Scott, Peter Jackson, and David Fincher. Conversely, the single English-language film with the highest number of votes, *The Shawshank Redemption*, has about 2.7 million votes, which is about 0.32% of all English votes. 

Though these are considerably large percentages, other languages appear to be far more likely to have dominating figures and films. Hayao Miyazaki, the Japanese animator and director behind Studio Ghibli, accounts for 22.3% of all Japanese-language votes, almost 13 magnitudes greater than Christopher Nolan’s proportion of English votes. 

*Parasite* alone, through its international success, makes up 13.8% of all Korean-language votes. Bong Joon Ho, the director of *Parasite*, takes over 26% of the total share of Korean votes. 

This appears in multiple languages, not just East Asian languages. For instance, when looking at the Danish language, 26% of all ratings come from the Academy Award winning director Thomas Vinterberg’s Danish films, such as *The Hunt* (2012) and *Another Round* (2020). 

This poses interesting questions about which films and individuals outside of Hollywood are able to gain traction. This phenomenon does not exist for all languages, but it is evident that the likelihood of a single film, director, or actor dominating a language’s film market is possible in non-English languages. At this point, however, it does not seem plausible for an English film to amass somewhere around 16 million votes. 

<img width="308" alt="Screen Shot 2023-05-04 at 12 56 28 PM" src="https://user-images.githubusercontent.com/105665462/236301976-64a59ff1-eaa6-42cf-bf1a-77d6fc466f59.png">
Figure 5: Languages grouped by director
<br> </br>

## Applications

The overall question explored in this project is whether certain conditions lead to greater user engagement with non-English films.  As previously articulated, this kind of engagement can be treated as a measure of success that is different from more traditional benchmarks such as box office proceeds or streaming views.  We also believe that a platform like IMDb can lead to users discovering film and television titles they might not otherwise come across.  With all of this in mind, our findings here can be applied in a number of different ways.
 
Perhaps the most obvious application is related to the potential investment in non-English film distribution in either the U.S. market or more globally.  Our research revealed that while still behind English films overall, there is certainly a market for non-English films among IMDb users.  Given a set amount of resources, our findings may help to decide which films should be prioritized. 
 
Our findings support some expected results—a film by an established director, for example, has a high chance of user engagement.  Taking this a step further, we suggest that based on our results any director that makes it into the IMDb Top 250 with a non-English film has an excellent chance of success with future films.  

Another applicable finding relates to the language itself.  We found that some languages appear to have an established market and therefore are a relatively safer bet: Spanish, French, German, Italian, and Japanese, for example.  This may be due in part to the number of speakers globally for each of the aforementioned languages, but our research indicates that it is not wholly responsible for their success.
 
Perhaps more unexpectedly, given our findings when it came to user votes, genres, and “underrated gems,” Indian language films may be a category with wide potential that has not yet been fully realized.  The recent relative commercial success of Telugu film *RRR* (Rajamouli, 2022) could be seen as a more concrete example of this.
 
Some genres may also be a more attractive investment choice when it comes to non-English films.  Drama in particular has had obvious and sustained success, while Documentary has seen a rise in popularity over the past three decades.  Our research also suggested that films involving the genre combination of Crime, Drama, and Mystery have also done well.
 
A second potential application involves marketing, specifically marketing on the IMDb platform.  We believe that our findings may help non-English films in choosing conditions that will encourage user engagement.  If you have a film involving crime or mystery, for example, it may be beneficial to categorize the genre as Crime/Drama/Mystery.  Additionally, if there are multiple languages spoken in the film it is certainly a positive to list all of them, rather than the main language.
 
Finally, our research could be applied with regards to IMDb users looking to discover new films.  The underrated gems on our list provide non-English films that are highly rated with enough user votes (according to our definition) to offset bias, but are not globally well-known.  IMDb’s capability of introducing users to films they might not otherwise discover has certainly helped with its longevity, and we believe that our findings may expand on this.

## Link to video demonstration
https://github.com/j-derrico/Spring-2023-Data-Mining-Project/blob/main/%20Group04_NonEnglishFilmEngagementonIMDb_part6_Video.mp4
## Link to final report
https://github.com/j-derrico/Spring-2023-Data-Mining-Project/blob/main/Group4_NonEnglishFilmEngagementOnIMDb_Part4.pdf
