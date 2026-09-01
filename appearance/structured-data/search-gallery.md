---
type: Reference
title: Structured data markup that Google Search supports
description: Explore the structured data-powered features that can appear in Google Search, including examples of how they appear in search results. Learn how to add structured data to help your site display in rich results on Google Search.
resource: https://developers.google.com/search/docs/appearance/structured-data/search-gallery
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:31:43Z'
sources:
- id: google-search-gallery
  resource: https://developers.google.com/search/docs/appearance/structured-data/search-gallery
  title: Structured data markup that Google Search supports
  author: Google Search Central (Google LLC)
  last_modified: '2026-06-15T00:00:00Z'
---

# Structured data markup that Google Search supports

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/search-gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-06-15.[^google-search-gallery]

Google uses [structured data](/appearance/structured-data/intro-structured-data.md) to understand the content on the page and show that content in a richer appearance in search results, which is called a *rich result*. To make your site eligible for appearance as one of these rich results, follow the guide to learn how to implement structured data on your site. If you're just getting started, visit [Understand how structured data works](/appearance/structured-data/intro-structured-data.md).

> **Note**: The actual appearance in search results might be different. You can preview most features with the [Rich Results Test](https://support.google.com/webmasters/answer/7445569).

Choose a category that describes your website Filter by... Ecommerce Organizations Sports Jobs Entertainment News Food and Drink Education and Science <table>
<thead>
<tr>
<th colspan="2">Structured data features</th>
<th>Filter column</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><b>Article</b></p>
<p>A news, sports, or blog article displayed in various rich result features, such as
                the title of the article and larger-than-thumbnail images.</p>
<a href="/appearance/structured-data/article.md">Get started</a>
</td>
<td>
<img alt="article example in search results" src="https://developers.google.com/static/search/docs/images/article-rich-result.png"/>
</td>
<td>News, Sports</td>
</tr>
<tr>
<td>
<p><b>Breadcrumb</b></p>
<p>Navigation that indicates the page's position in the site hierarchy.</p>
<a href="/appearance/structured-data/breadcrumb.md">Get started</a>
</td>
<td>
<img alt="breadcrumb example in search results" src="https://developers.google.com/static/search/docs/images/breadcrumb.png"/>
</td>
<td>Generic</td>
</tr>
<tr>
<td>
<p><b>Carousel</b></p>
<p>Rich results that display in a sequential list or gallery from a single site. This
                feature must be combined with one of the following features:
                <a href="/appearance/structured-data/recipe.md">Recipe</a>,
                <a href="/appearance/structured-data/course.md">Course list</a>,
                <a href="/appearance/structured-data/local-business.md">Restaurant</a>,
                <a href="/appearance/structured-data/movie.md">Movie</a>.</p>
<a href="/appearance/structured-data/carousel.md">Get started</a>
</td>
<td>
<img alt="An illustration of how a recipe host carousel can appear in Google Search. It shows 3 different recipes from the same website in a carousel format that users can explore and select a specific recipe" src="https://developers.google.com/static/search/docs/images/recipe-host-carousel-rich-result.png"/>
</td>
<td>Food and Drink, Education and Science, Entertaiment</td>
</tr>
<tr>
<td>
<p><b>Course list</b></p>
<p>A list of educational course from the same course provider. Courses can include
                the course title, provider, and a short description.</p>
<a href="/appearance/structured-data/course.md">Get started</a>
</td>
<td>
<img alt="course list rich result in search results" src="https://developers.google.com/static/search/docs/images/course-carousel-rich-result.png"/>
</td>
<td>Education and Science</td>
</tr>
<tr>
<td>
<p><b>Dataset</b></p>
<p>Large data sets that appear in Google Dataset Search.</p>
<a href="/appearance/structured-data/dataset.md">Get started</a>
</td>
<td>
<img alt="dataset example in search results" src="https://developers.google.com/static/search/docs/images/dataset-search.png"/>
</td>
<td>Education and Science</td>
</tr>
<tr>
<td>
<p><b>Discussion forum</b></p>
<p>User-generated content (traditionally short-form compared to <code>Article</code>),
                followed by a threaded or non-threaded discussion about that topic.</p>
<a href="/appearance/structured-data/discussion-forum.md">Get started</a>
</td>
<td>
<img alt="An illustration of the discussions and forums rich result" src="https://developers.google.com/static/search/docs/images/discussions-and-forums-rich-result.png"/>
</td>
<td></td>
</tr>
<tr>
<td>
<p><b>Education Q&amp;A</b></p>
<p>Education-related questions and answers that help students discover flashcards on Google Search.</p>
<a href="/appearance/structured-data/education-qa.md">Get started</a>
</td>
<td>
<img alt="Education Q&amp;A carousel in search results" src="https://developers.google.com/static/search/docs/images/education-qa-rich-result.png"/>
</td>
<td>Education and Science</td>
</tr>
<tr>
<td>
<p><b>Employer aggregate rating</b></p>
<p>An evaluation of a hiring organization compiled from many users that's displayed in
                the job search experience on Google.</p>
<a href="/appearance/structured-data/employer-rating.md">Get started</a>
</td>
<td>
<img alt="employer aggregate rating example in search results" src="https://developers.google.com/static/search/docs/images/employer-aggregate-rating01.png"/>
</td>
<td>Jobs</td>
</tr>
<tr>
<td>
<p><b>Event</b></p>
<p>An interactive rich result that shows a list of organized events, such as concerts
                or art festivals, that people may attend at a particular time and place.</p>
<a href="/appearance/structured-data/event.md">Get started</a>
</td>
<td>
<img alt="How the event experience looks on Google Search" src="https://developers.google.com/static/search/docs/images/event-rich-result.png"/>
</td>
<td>Entertainment</td>
</tr>
<tr>
<td>
<p><b>Image metadata</b></p>
<p>When you specify image metadata, Google Images can show more details about the image,
                such as who the creator is, how people can use an image, and credit information.</p>
<a href="/appearance/structured-data/image-license-metadata.md">Get started</a>
<td><img alt="An example of Image Metadata in Google Images" src="https://developers.google.com/static/search/docs/images/image-metadata.png"/></td>
<td></td>
</td></tr>
<tr>
<td>
<p><b>Job posting</b></p>
<p>An interactive rich result that allows job seekers to find a job. The job search
                experience on Google can feature your logo, reviews, ratings, and job details.</p>
<a href="/appearance/structured-data/job-posting.md">Get started</a>
<td>
<img alt="job posting example in search results" src="https://developers.google.com/static/search/docs/images/jobs-search-ui.png"/>
</td>
<td>Jobs</td>
</td></tr>
<tr>
<td>
<p><b>Local business</b></p>
<p>Business details displayed in the Google knowledge panel, including open hours,
                ratings, directions, and actions to book appointments or order items.</p>
<a href="/appearance/structured-data/local-business.md">Get started</a>
</td>
<td>
<img alt="local business example in search results" src="https://developers.google.com/static/search/docs/images/local-business02.png"/>
</td>
<td>Organizations</td>
</tr>
<tr>
<td>
<p><b>Math solver</b></p>
<p>Help students, teachers, and others with math problems by adding structured data to
                indicate the type of math problems and step-by-step walkthroughs for specific math problems.</p>
<a href="/appearance/structured-data/math-solvers.md">Get started</a>
</td>
<td>
<img alt="math solvers in search results" src="https://developers.google.com/static/search/docs/images/math-solvers-rich-result.png"/>
</td>
<td>Education and Science</td>
</tr>
<tr>
<td>
<p><b>Movie</b></p>
<p>The movie carousel helps users explore lists of movies on Google Search (for example,
           "best movies of 2023"). You can provide details about the movies, such as the title of
           each movie, director information, and images.</p>
<a href="/appearance/structured-data/movie.md">Get started</a>
</td>
<td>
<img alt="An illustration of how a movie rich result can appear in Google Search. It shows 3 different movies from the same website in a carousel format that users can explore and select a specific movie" src="https://developers.google.com/static/search/docs/images/movie-rich-result.png"/>
</td>
<td>Entertainment</td>
</tr>
<tr>
<td>
<p><b>Organization</b></p>
<p>Information about your organization, such as your logo, legal name of the
                organization, address, contact information, and company identifiers. This information
                can show up in knowledge panels and other visual elements (such as
                <a href="/appearance/visual-elements-gallery.md">attribution</a>).
              </p>
<a href="/appearance/structured-data/organization.md">Get started</a>
</td>
<td>
<img alt="organization example in search results" src="https://developers.google.com/static/search/docs/images/organization.png"/>
</td>
<td>Organizations</td>
</tr>
<tr>
<td>
<p><b>Product</b></p>
<p>Information about a product, including price, availability, and review ratings.</p>
<a href="/appearance/structured-data/product.md">Get started</a>
</td>
<td>
<img alt="product example in search results" src="https://developers.google.com/static/search/docs/images/search-gallery-products.png"/>
</td>
<td>Ecommerce</td>
</tr>
<tr>
<td>
<p><b>Profile page</b></p>
<p>A page that primarily focuses on information about a single person or organization
                that is somehow affiliated with the overall website.</p>
<a href="/appearance/structured-data/profile-page.md">Get started</a>
</td>
<td>
<img alt="An illustration of the Perspectives filter in search results" src="https://developers.google.com/static/search/docs/images/discussions-and-forums-rich-result.png"/>
</td>
<td></td>
</tr>
<tr>
<td>
<p><b>Q&amp;A</b></p>
<p>Q&amp;A Pages are web pages that contain data in a question and answer format,
                which is one question followed by its answers.</p>
<a href="/appearance/structured-data/qapage.md">Get started</a>
</td>
<td>
<img alt="question answer page example in search results" src="https://developers.google.com/static/search/docs/images/qa-example-screenshot.png"/>
</td>
<td></td>
</tr>
<tr>
<td>
<p><b>Recipe</b></p>
<p>Recipes that display as an individual rich result or part of a host carousel.</p>
<a href="/appearance/structured-data/recipe.md">Get started</a>
</td>
<td>
<img alt="An illustration of how a recipe host carousel can appear in Google Search. It shows 3 different recipes from the same website in a carousel format that users can explore and select a specific recipe" src="https://developers.google.com/static/search/docs/images/recipe-host-carousel-rich-result.png"/>
</td>
<td>Food and Drink</td>
</tr>
<tr>
<td>
<p><b>Review snippet</b></p>
<p>A short excerpt of a review or a rating from a review website, usually an average
                of the combined rating scores from reviewers. A review snippet can be about
                <a href="/appearance/structured-data/book.md">Book</a>,
                <a href="/appearance/structured-data/recipe.md">Recipe</a>,
                <a href="/appearance/structured-data/movie.md">Movie</a>,
                <a href="/appearance/structured-data/product.md">Product</a>,
                <a href="/appearance/structured-data/software-app.md">Software App</a>,
                and <a href="/appearance/structured-data/local-business.md">Local business</a>.
              </p>
<a href="/appearance/structured-data/review-snippet.md">Get started</a>
</td>
<td>
<img alt="review snippet example in search results" src="https://developers.google.com/static/search/docs/images/search-gallery-reviews.png"/>
</td>
<td>
              Organizations, Ecommerce, Food and Drink, Entertainment
            </td>
</tr>
<tr>
<td>
<p><b>Software app</b></p>
<p>Information about a software app, including rating information, a description of
                the app, and a link to the app.</p>
<a href="/appearance/structured-data/software-app.md">Get started</a>
</td>
<td>
<img alt="software app example in search results" src="https://developers.google.com/static/search/docs/images/software-apps.png"/>
</td>
<td></td>
</tr>
<tr>
<td>
<p><b>Speakable</b></p>
<p>Allow search engines and other applications to identify news content to read aloud
                on Google Assistant-enabled devices using text-to-speech (TTS).</p>
<a href="/appearance/structured-data/speakable.md">Get started</a>
</td>
<td>
<img alt="speakable example that shows a conversation with the Google Home. A person
                        asks Google Home what's the latest news with Nasa. Google Home responds with
                        a list of three news articles." src="https://developers.google.com/static/search/docs/images/search-gallery-speakable.png"/>
</td>
<td>News</td>
</tr>
<tr>
<td>
<p><b>Subscription and paywalled content</b></p>
<p>Indicate paywalled content on your site to help Google differentiate paywalled
                content from the practice of
                <a href="/essentials/spam-policies.md">cloaking</a>, which violates
                <a href="/essentials/spam-policies.md">our spam policies</a>.
              </p>
<a href="/appearance/structured-data/paywalled-content.md">Get started</a>
</td>
<td>
<img alt="A New York Times paywall example that shows a reader has reached the limit
                        of articles" src="https://developers.google.com/static/search/docs/images/search-gallery-paywall.png"/>
</td>
<td>News</td>
</tr>
<tr>
<td>
<p><b>Vacation rental</b></p>
<p>Information about a vacation property, such as the name, description,
                images, location, rating, and reviews.</p>
<a href="/appearance/structured-data/vacation-rental.md">Get started</a>
</td>
<td>
<img alt="illustration of a vacation rental rich result" src="https://developers.google.com/static/search/docs/images/vacation-rental-rich-result.png"/>
</td>
<td>
</td>
</tr>
<tr>
<td>
<p><b>Video</b></p>
<p>Video information in search results, with the option to play the video, specify video
           segments, and live-stream content.</p>
<a href="/appearance/structured-data/video.md">Get started</a>
</td>
<td>
<img alt="video example in search results" src="https://developers.google.com/static/search/docs/images/video-key-moments.png"/>
</td>
<td>
              Food and Drink, News, Education and Science, Sports
            </td>
</tr>
</tbody>
</table>

# References & Citations

[^google-search-gallery]: Google Search Central (2026). "Structured data markup that Google Search supports". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/search-gallery. Retrieved 2026-09-01.
