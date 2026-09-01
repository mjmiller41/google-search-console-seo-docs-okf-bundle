---
type: Reference
title: Recipe (Recipe,HowTo,ItemList) structured data
description: You can help users find your recipe by telling Google about your recipe reviews, cook time, and nutrition information with structured data.
resource: https://developers.google.com/search/docs/appearance/structured-data/recipe
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-recipe
  resource: https://developers.google.com/search/docs/appearance/structured-data/recipe
  title: Recipe (Recipe,HowTo,ItemList) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Recipe (Recipe,HowTo,ItemList) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/recipe](https://developers.google.com/search/docs/appearance/structured-data/recipe). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-recipe]

Help users find your recipe content by telling Google about your recipe with structured data. When you provide information such as reviewer ratings, cooking and preparation times, and nutrition information, Google can better understand your recipe and present it to users in interesting ways. Recipes can appear in Google Search results and Google Images.

![An illustration of how recipe rich results can appear in Google Search. It contains 4 rich results from different websites, with details about how long it takes to cook the recipe, an image, and review information.](https://developers.google.com/static/search/docs/images/recipe-rich-result-google-search.png) ![An illustration of how a recipes can appear in Google Images. There are 6 images results showing different food items, with 3 results containing a recipe badge that tells the user it's a recipe](https://developers.google.com/static/search/docs/images/recipes-in-google-images.png)

Based on how you mark up your content, your recipes can be eligible for the following enhancements:

<table>
<tbody>
<th colspan="2"><b>Recipe enhancements</b></th>
<tr>
<td><b>Recipe host carousel</b>: Enable users to explore your recipe gallery
          pages by adding <a href="https://developers.google.com/search/docs/appearance/structured-data/recipe/#item-list"><code>ItemList</code> structured data</a>.
          </td>
<td>
<img alt="An illustration of how a recipe host carousel can appear in Google Search. It shows 3 different recipes from the same website in a carousel format that users can explore and select a specific recipe" src="https://developers.google.com/static/search/docs/images/recipe-host-carousel-rich-result.png">
</img></td>
</tr>
</tbody>
</table>

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add the [required properties](https://developers.google.com/search/docs/appearance/structured-data/recipe/#structured-data-type-definitions). Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/recipe/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Examples

Here are some examples of recipes using JSON-LD code.

> **Note**: The actual appearance in Search results might be different. Preview the structured data in the Rich Results Test for the most up-to-date layout.

### Recipe on Search

Here's an example of a page that's eligible to be displayed on Search.

``` devsite-click-to-copy
<html>
  <head>
    <title>Non-Alcoholic Piña Colada</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org/",
      "@type": "Recipe",
      "name": "Non-Alcoholic Piña Colada",
      "image": [
      "https://example.com/photos/1x1/photo.jpg",
      "https://example.com/photos/4x3/photo.jpg",
      "https://example.com/photos/16x9/photo.jpg"
      ],
      "author": {
        "@type": "Person",
        "name": "Mary Stone"
      },
      "datePublished": "2024-03-10",
      "description": "This non-alcoholic pina colada is everyone's favorite!",
      "recipeCuisine": "American",
      "prepTime": "PT1M",
      "cookTime": "PT2M",
      "totalTime": "PT3M",
      "keywords": "non-alcoholic",
      "recipeYield": "4 servings",
      "recipeCategory": "Drink",
      "nutrition": {
        "@type": "NutritionInformation",
        "calories": "120 calories"
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 5,
        "ratingCount": 18
      },
      "recipeIngredient": [
        "400ml of pineapple juice",
        "100ml cream of coconut",
        "ice"
      ],
      "recipeInstructions": [
        {
          "@type": "HowToStep",
          "name": "Blend",
          "text": "Blend 400ml of pineapple juice and 100ml cream of coconut until smooth.",
          "url": "https://example.com/non-alcoholic-pina-colada#step1",
          "image": "https://example.com/photos/non-alcoholic-pina-colada/step1.jpg"
        },
        {
          "@type": "HowToStep",
          "name": "Fill",
          "text": "Fill a glass with ice.",
          "url": "https://example.com/non-alcoholic-pina-colada#step2",
          "image": "https://example.com/photos/non-alcoholic-pina-colada/step2.jpg"
        },
        {
          "@type": "HowToStep",
          "name": "Pour",
          "text": "Pour the pineapple juice and coconut mixture over ice.",
          "url": "https://example.com/non-alcoholic-pina-colada#step3",
          "image": "https://example.com/photos/non-alcoholic-pina-colada/step3.jpg"
        }
      ],
      "video": {
        "@type": "VideoObject",
        "name": "How to Make a Non-Alcoholic Piña Colada",
        "description": "This is how you make a non-alcoholic piña colada.",
        "thumbnailUrl": [
          "https://example.com/photos/1x1/photo.jpg",
          "https://example.com/photos/4x3/photo.jpg",
          "https://example.com/photos/16x9/photo.jpg"
         ],
        "contentUrl": "https://www.example.com/video123.mp4",
        "embedUrl": "https://www.example.com/videoplayer?video=123",
        "uploadDate": "2024-02-05T08:00:00+08:00",
        "duration": "PT1M33S",
        "interactionStatistic": {
          "@type": "InteractionCounter",
          "interactionType": { "@type": "WatchAction" },
          "userInteractionCount": 2347
        },
        "expires": "2024-02-05T08:00:00+08:00"
       }
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

### Carousel

Here's an example of a recipe summary page (a page with a list of recipes) with [`itemList`](https://developers.google.com/search/docs/appearance/structured-data/recipe/#item-list) structured data. This content may be eligible to be displayed in a grid in Search results.

``` devsite-click-to-copy
<html>
  <head>
    <title>Grandma's Best Pie Recipes</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "ItemList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "url": "https://example.com/apple-pie.html"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "url": "https://example.com/blueberry-pie.html"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "url": "https://example.com/cherry-pie.html"
        }]
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

## Guidelines

You must follow the [general structured data guidelines](/appearance/structured-data/sd-policies.md) for your markup to be eligible to appear in Search results.

> If you violate these policies, your recipe might not show up as a rich result, but your content will still appear in Search results. Read about [Spammy Structured Markup](https://support.google.com/webmasters/answer/3498001).

The following guidelines apply to `Recipe` structured data.

- Use `Recipe` structured data for content about preparing a particular dish. For example, "facial scrub" or "party ideas" are not valid names for a dish.
- To enable your recipes to appear in a [carousel](/appearance/structured-data/carousel.md) or grid, you must follow these guidelines:
  - Provide `ItemList` structured data to summarize the recipes for your list. You can provide `ItemList` structured data separately or together with recipe structured data.
  - Your site must have a summary page that lists all the recipes in the collection. For example, when a user clicks the summary link from Search results, they are properly directed to a page on your site listing the recipes related to their search.

## Structured data type definitions

You must include the required properties for your content to be eligible for display as a rich result in Google Search. You can also include the recommended properties to add more information about your content, which could provide a better user experience.

### `Recipe`

Mark up your recipe content with the following properties of the schema.org [`Recipe`](https://schema.org/Recipe) type. The full definition of `Recipe` is available at [schema.org/Recipe](https://schema.org/Recipe). The Google-supported properties are the following:

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td>
<code>image</code>
</td>
<td><p><code><a href="https://schema.org/URL">URL</a></code> or <code><a href="https://schema.org/ImageObject">ImageObject</a></code></p>
<p>Image of the completed dish.</p>
<p>Additional image guidelines:
  <ul>
<li>Image URLs must be crawlable and indexable. To check if Google can access your URLs, use
      the <a href="https://support.google.com/webmasters/answer/9012289">URL Inspection tool</a>.</li>
<li>Images must represent the marked up content.</li>
<li>Images must be in a file format that's <a href="/appearance/google-images.md">supported by Google Images</a>.</li>
<li>For best results, we recommend providing multiple high-resolution images (minimum of 50K pixels when
      multiplying width and height) with the following aspect ratios: 16x9, 4x3, and 1x1.</li>
</ul>
<p>For example:</p>
<pre class="devsite-click-to-copy">"image": [
  "https://example.com/photos/1x1/photo.jpg",
  "https://example.com/photos/4x3/photo.jpg",
  "https://example.com/photos/16x9/photo.jpg"
]</pre>
<blockquote>Specifying the <code>image</code> property in <code>Recipe</code> markup
            has no impact on the image chosen for a <a href="/appearance/visual-elements-gallery.md">text result image</a>.
            To optimize for a text result image, follow the <a href="/appearance/google-images.md">image SEO best practices</a>.</blockquote>
</p></td>
</tr>
<tr>
<td><code>name</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The name of the dish.</p></td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Recommended properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>aggregateRating</code></td>
<td><p><code><a href="https://schema.org/AggregateRating">AggregateRating</a></code></p>
<p>Annotation for the average review score assigned to the item. Follow the <a href="/appearance/structured-data/review-snippet.md">Review snippet guidelines</a> and list of required and recommended <a href="/appearance/structured-data/review-snippet.md"><code>AggregateRating</code> properties</a>.</p>
<p>If the <code>Recipe</code> structured data contains a single review, the reviewer's name must be a valid
              person or organization. For example, "50% off ingredients" is not a valid name for a
              reviewer.</p></td>
</tr>
<tr>
<td><code>author</code></td>
<td><p><code><a href="https://schema.org/Person">Person</a></code>
              or <code><a href="https://schema.org/Organization">Organization</a></code></p>
<p>The name of the person or organization that wrote the recipe. To help Google best
            understand authors across various features, consider following the
            <a href="/appearance/structured-data/article.md">author markup best practices</a>.</p></td>
</tr>
<tr>
<td><code>cookTime</code></td>
<td><p><code><a href="https://schema.org/Duration">Duration</a></code></p>
<p>The time it takes to actually cook the dish in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>, if applicable.
            </p>
<p>Always use in combination with <code>prepTime</code>. </p></td>
</tr>
<tr>
<td><code>datePublished</code></td>
<td><p><code><a href="https://schema.org/Date">Date</a></code></p>
<p>The date the recipe was published in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>,
            if applicable.</p></td>
</tr>
<tr>
<td><code>description</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>A short summary describing the dish.</p></td>
</tr>
<tr>
<td>
<code>keywords</code>
</td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>Other terms for your recipe such as the season ("summer"), the holiday ("Halloween"), or other descriptors ("quick", "easy", "authentic").</p>
<p><b>Additional guidelines</b></p>
<ul>
<li>Separate multiple entries in a keywords list with commas.</li>
<li>Don't use a tag that's actually a <code>recipeCategory</code>
            or <code>recipeCuisine</code>.
                <br/>
<p><b>Not recommended</b>:</p>
<pre class="devsite-click-to-copy">"keywords": "dessert, American"</pre>
<p><b>Recommended</b>:</p>
<pre class="devsite-click-to-copy">"keywords": "winter apple pie, nutmeg crust"</pre></li>
</ul>
</td>
</tr>
<tr>
<td><code>nutrition.calories</code></td>
<td><p><code><a href="https://schema.org/Energy">Energy</a></code></p>
<p>The number of calories in each serving produced with this
          recipe. If <code>nutrition.calories</code> is defined, <code>recipeYield</code> must be defined
          with the number of servings.</p></td>
</tr>
<tr>
<td><code>prepTime</code></td>
<td>
<p>
<code><a href="https://schema.org/Duration">Duration</a></code>
</p>
<p>
              The length of time it takes to prepare ingredients and workspace for the dish, in
              <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>,
              if applicable.
            </p>
<p>Always use in combination with <code>cookTime</code>.</p>
</td>
</tr>
<tr>
<td><code>recipeCategory</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The type of meal or course your recipe is about. For example: "dinner", "main course", or "dessert, snack".</p></td>
</tr>
<tr>
<td><code>recipeCuisine</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The region associated with your recipe. For example, "French", Mediterranean", or "American".</p></td>
</tr>
<tr>
<td><code>recipeIngredient</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code>
<p>An ingredient used in the recipe. </p>
<p>For example:</p>
<pre class="devsite-click-to-copy">"recipeIngredient": [
  "1 (15 ounce) package double crust ready-to-use pie crust",
  "6 cups thinly sliced, peeled apples (6 medium)",
  "3/4 cup sugar",
  "2 tablespoons all-purpose flour",
  "3/4 teaspoon ground cinnamon",
  "1/4 teaspoon salt",
  "1/8 teaspoon ground nutmeg",
  "1 tablespoon lemon juice"
]</pre>
<p><b>Additional guidelines</b>:</p>
<ul>
<li>Include only the ingredient text that is necessary for making the recipe. </li>
<li>Don't include unnecessary information, such as a definition of the ingredient. </li>
</ul>
</p></td>
</tr>
<tr>
<td><code>recipeInstructions</code>
</td>
<td><p><code><a href="https://schema.org/HowToStep">HowToStep</a></code>, <code><a href="https://schema.org/HowToSection">HowToSection</a></code>, or <code><a href="https://schema.org/Text">Text</a></code>
<p>The steps to make the dish.</p>
<p>There are several options for setting the value of <code>recipeInstructions</code>. We recommend using <code>HowToStep</code>. <code>HowToSection</code> can also be used to group HowToSteps when the recipe has sections.</p>
<ul>
<li><b><code>HowToStep</code></b>: Specify this recipe's steps with <code>HowToStep</code>.
            <pre class="devsite-click-to-copy">"recipeInstructions": [
  {
    "@type": "HowToStep",
    "name": "Preheat",
    "text": "Heat oven to 425°F.",
    "url": "https://example.com/recipe#step1",
    "image": "https://example.com/photos/recipe/step1.jpg"
  }, {
    "@type": "HowToStep",
    "name": "Prepare crust",
    "text": "Place 1 pie crust in ungreased 9-inch glass pie plate, pressing firmly against side and bottom.",
    "url": "https://example.com/recipe#step2",
    "image": "https://example.com/photos/recipe/step2.jpg"
  }, {
    "@type": "HowToStep",
    "name": "Make filling",
    "text": "In large bowl, gently mix filling ingredients; spoon into crust-lined pie plate.",
    "url": "https://example.com/recipe#step3",
    "image": "https://example.com/photos/recipe/step3.jpg"
  }, {
    "@type": "HowToStep",
    "name": "Cover",
    "text": "Top with second crust. Cut slits or shapes in several places in top crust.",
    "url": "https://example.com/recipe#step4",
    "image": "https://example.com/photos/recipe/step4.jpg"
  }, {
    "@type": "HowToStep",
    "name": "Bake",
    "text": "Bake 40 to 45 minutes. The pie is ready when the apples are tender and the crust is golden brown.",
    "url": "https://example.com/recipe#step5",
    "image": "https://example.com/photos/recipe/step5.jpg"
  }, {
    "@type": "HowToStep",
    "name": "Cool",
    "text": "Cool on cooling rack at least 2 hours before serving.",
    "url": "https://example.com/recipe#step6",
    "image": "https://example.com/photos/recipe/step6.jpg"
  }
]</pre>
</li>
<li><b><code>HowToSection</code> (only if a recipe has multiple sections)</b>:
                Use to group steps into multiple sections. See <code><a href="https://developers.google.com/search/docs/appearance/structured-data/recipe/#how-to-section">HowToSection</a></code> for an example.
              </li>
<li><b>Single or repeated property of text</b>: A block of text that includes one or more steps. Google treats all steps as being in a single section. Repeated
                property values are concatenated into a single block of text. Google then attempts to
                automatically split the single block of text into individual steps. Google tries to
                find and remove any section names, step numbers, keywords, and anything else that
                can incorrectly appear in recipe step text. For best results, we recommend you
                unambiguously specify steps with <code><a href="https://developers.google.com/search/docs/appearance/structured-data/recipe/#how-to-step">HowToStep</a></code>.
            <pre class="devsite-click-to-copy">"recipeInstructions": [
  "In large bowl, gently mix filling ingredients; spoon into crust-lined pie
plate. Top with second crust. Cut slits or shapes in several places in top
crust. Bake 40 to 45 minutes. The pie is ready when the or until apples are
tender and the crust is golden brown. Cool on cooling rack at least 2 hours
before serving."
]</pre>
</li>
</ul>
<p><b>Additional guidelines</b></p>
<ul>
<li>Don't include metadata that belongs elsewhere. In particular, use the <code>author</code>
                property to specify the author, <code>recipeCuisine</code> for cuisine,
                <code>recipeCategory</code> for category, and <code>keywords</code> for other keywords.</li>
<li>Include only text on how to make the dish and don't include other text such as
                "Directions", "Watch the video", "Step 1". Specify those phrases
                outside of structured data.
              <p><b>Not recommended</b>:</p>
<pre class="devsite-click-to-copy devsite-code-highlight">"recipeInstructions": [{
  "@type": "HowToStep",
  <strong>"text": "Step 1. Heat oven to 425°F."</strong>
}]</pre>
<p><b>Recommended</b>:</p>
<pre class="devsite-click-to-copy devsite-code-highlight">"recipeInstructions": [{
  "@type": "HowToStep",
  <strong>"text": "Heat oven to 425°F."</strong>
}]</pre>
</li>
</ul>
</p></td>
</tr>
<tr>
<td><code>recipeYield</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code> or <code><a href="https://schema.org/Integer">Integer</a></code></p>
<p>The quantity produced by the recipe, if applicable. Specify the number of servings
            produced from this recipe with just a number. If you wish to use a different unit (for
            example, number of items), you may include additional yields. This is required if you
            specify any nutritional information per serving (such as <code>nutrition.calories</code>).
            <p>Example</p>
<pre class="devsite-click-to-copy">"recipeYield": [
  "6",
  "24 cookies"
]</pre>
</p></td>
</tr>
<tr>
<td><code>totalTime</code></td>
<td><p><code><a href="https://schema.org/Duration">Duration</a></code></p>
<p>The total time it takes to prepare
            the cook the dish, in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>, if applicable.
          </p>
<p>Use <code>totalTime</code> or a combination of both <code>cookTime</code> and <code>prepTime</code>. </p> </td>
</tr>
<tr>
<td>
<code>video</code>
</td>
<td><code><a href="https://schema.org/VideoObject">VideoObject</a></code>
<p>
          A video depicting the steps to make the dish. Follow the list of required and recommended
            <a href="/appearance/structured-data/video.md">Video properties</a>.
        </p>
</td></tr>
</tbody>
</table>

### `HowToSection`

> Most recipes don't have sections. Start by splitting the recipe instructions into `HowToStep` properties, and only add `HowToSection` if you need to additionally specify sections of steps.

Use `HowToSection` to group a sequence of steps (or sub-sections) that make up part of the instructions for a recipe. Specify `HowToSection` directly within the definition of `recipeInstructions` property, or as an `itemListElement` of another `HowToSection`.

The `HowToSection` type defines a section of a single recipe and contains one or multiple steps. Don't use `HowToSection` to define different recipes for the same dish; instead, use `HowToSection` as part of a single recipe. For listing multiple recipes for a dish, use multiple `Recipe` objects. For example, for multiple ways to make an apple pie, list them as multiple `Recipe` objects, not `HowToSection` objects.

The full definition of `HowToSection` is available at [schema.org/HowToSection](https://schema.org/HowToSection).

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td>
<code>itemListElement</code>
</td>
<td><code><a href="https://developers.google.com/search/docs/appearance/structured-data/recipe/#how-to-step">HowToStep</a></code>
<p>A list of detailed steps for the section, and/or sub-sections. For example, a pizza recipe may have
        one section of steps for making the crust, one for preparing the
        toppings, and one for combining and baking.</p>
<p>Example:</p>
<pre class="devsite-click-to-copy">{
  "@type": "HowToSection",
  "name": "Assemble the pie",
  "itemListElement": [
    {
      "@type": "HowToStep",
      "text": "In large bowl, gently mix filling ingredients; spoon into crust-lined pie plate."
    }, {
      "@type": "HowToStep",
      "text": "Top with second crust. Cut slits or shapes in several places in top crust."
    }
  ]
}</pre>
</td>
</tr>
<tr>
<td>
<code>name</code>
</td>
<td><code><a href="https://schema.org/Text">Text</a></code>
<p>The name of the section.</p>
</td>
</tr>
</tbody>
</table>

### `HowToStep`

Use `HowToStep` to group one or more sentences that explain how to do part of the recipe, if this makes sense for your content. Define the `text` property with the sentences or, alternately, define `itemListElement` with a `HowToDirection` or `HowToTip` for each sentence.

Mark up your recipe steps with the following properties of the [HowToStep](https://schema.org/HowToStep) type. Specify a `HowToStep` directly within the definition of `recipeInstructions` property, or as an `itemListElement` of a `HowToSection`.

The full definition of `HowToStep` is available at [schema.org/HowToStep](https://schema.org/HowToStep).

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td>
<code>itemListElement</code>
</td>
<td><code><a href="https://schema.org/HowToDirection">HowToDirection</a></code> or <code><a href="https://schema.org/HowToTip">HowToTip</a></code>
<p>A list of detailed substeps, including directions or tips.</p>
<p>Optional if <code>text</code> is used.</p>
</td>
</tr>
<tr>
<td>
<code>text</code>
</td>
<td><code><a href="https://schema.org/Text">Text</a></code>
<p>The full instruction text of this step.</p>
<p>Optional if <code>itemListElement</code> is used. Additional guidelines:</p>
<ul>
<li>Include only instructional text and don't include other text such as
            "Directions", "Watch the video", "Step 1". Specify those phrases outside of the marked
            up property.
            <br/>
<p><b>Not recommended</b>:</p>
<pre class="devsite-click-to-copy devsite-code-highlight">{
  "@type": "HowToStep",
  <strong>"text": "Step 1. Heat oven to 425°F."</strong>
}</pre>
<p><b>Recommended</b>:</p>
<pre class="devsite-click-to-copy devsite-code-highlight">{
  "@type": "HowToStep",
  <strong>"text": "Heat oven to 425°F."</strong>
}</pre>
</li>
</ul>
</td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Recommended properties</th></tr>
</thead>
<tbody>
<tr>
<td>
<code>image</code>
</td>
<td><code><a href="https://schema.org/ImageObject">ImageObject</a></code> or <code><a href="https://schema.org/URL">URL</a></code>
<p>
          An image for the step. Additional image guidelines:
        </p>
<ul>
<li>Image URLs must be <a href="/crawling-indexing/sitemaps/image-sitemaps.md">crawlable and indexable</a>.</li>
<li>Images must represent the marked up content.</li>
<li>Images must be in .jpg, .png, or. gif format.</li>
</ul>
</td>
</tr>
<tr>
<td>
<code>name</code>
</td>
<td><code><a href="https://schema.org/Text">Text</a></code>
<p>
          The word or short phrase summarizing the step (for example, "Arrange pie crust").
          Don't use non-descriptive text (for example, "Step 1: [text]") or other form of step number
          (for example, "1. [text]").
        </p>
</td>
</tr>
<tr>
<td>
<code>url</code>
</td>
<td><code><a href="https://schema.org/URL">URL</a></code>
<p>
          A <code>URL</code> that directly links to the step (if one is available). For example,
          an anchor link fragment.
        </p>
</td>
</tr>
<tr>
<td>
<code>video</code>
</td>
<td><code><a href="https://schema.org/VideoObject">VideoObject</a></code> or <code><a href="https://schema.org/Clip">Clip</a></code>
<p> A video for this step or a clip of the video. </p>
<p> For <code><a href="https://schema.org/VideoObject">VideoObject</a></code>, follow the list of required and recommended
          <a href="/appearance/structured-data/video.md">Video</a>
          or <a href="/appearance/structured-data/video.md">Clip</a> properties.
        </p>
</td>
</tr>
</tbody>
</table>

### `HowToDirection` and `HowToTip`

Use `HowToDirection` and `HowToTip` to describe directions or tips, if applicable. They have the same required and recommended properties.

The full definitions of `HowToDirection` and `HowToTip` are available at [schema.org/HowToDirection](https://schema.org/HowToDirection) and [schema.org/HowToTip](https://schema.org/HowToTip).

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td>
<code>text</code>
</td>
<td><code><a href="https://schema.org/Text">Text</a></code>
<p>The text of the direction or tip.</p>
</td>
</tr>
</tbody>
</table>

### `ItemList`

In addition to [Recipe properties](https://developers.google.com/search/docs/appearance/structured-data/recipe/#recipe-properties), add the following properties for host-specific lists. While `ItemList` isn't required, you must add the following properties if you want your recipe to be eligible for a host carousel. For more information about host carousel, see [Carousel](/appearance/structured-data/carousel.md).

The full definition of `ItemList` is available at [schema.org/ItemList](https://schema.org/ItemList).

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td>
<code>itemListElement</code>
</td>
<td><p><code><a href="https://schema.org/ListItem">ListItem</a></code></p>
<p>Annotation for a single item page.</p></td>
</tr>
<tr>
<td>
<code>ListItem.position</code>
</td>
<td><p><code><a href="https://schema.org/Integer">Integer</a></code></p>
<p>Ordinal position of the item page in the list. For example:</p>
<pre class="pretty-print">
"itemListElement": [
  {
    "@type": "ListItem",
    <strong>"position": 1,</strong>
  }, {
    "@type": "ListItem",
    <strong>"position": 2,</strong>
  }
]
</pre>
</td>
</tr>
<tr>
<td>
<code>ListItem.url</code>
</td>
<td><p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>The canonical URL of the item page. Every item must have a unique URL.</p></td>
</tr>
</tbody>
</table>

## Monitor rich results with Search Console

Search Console is a tool that helps you monitor how your pages perform in Google Search. You don't have to sign up for Search Console to be included in Google Search results, but it can help you understand and improve how Google sees your site. We recommend checking Search Console in the following cases:

1.  [After deploying structured data for the first time](https://developers.google.com/search/docs/appearance/structured-data/recipe/#after-deploying)
2.  [After releasing new templates or updating your code](https://developers.google.com/search/docs/appearance/structured-data/recipe/#after-releasing)
3.  [Analyzing traffic periodically](https://developers.google.com/search/docs/appearance/structured-data/recipe/#analyzing-periodically)

### After deploying structured data for the first time

After Google has indexed your pages, look for issues using the relevant [Rich result status report](https://support.google.com/webmasters/answer/7552505). Ideally, there will be an increase of valid items, and no increase in invalid items. If you find issues in your structured data:

1.  [Fix the invalid items](https://developers.google.com/search/docs/appearance/structured-data/recipe/#troubleshooting).
2.  [Inspect a live URL](https://support.google.com/webmasters/answer/9012289#test_live_page) to check if the issue persists.
3.  [Request validation](https://support.google.com/webmasters/answer/13300208) using the status report.

### After releasing new templates or updating your code

When you make significant changes to your website, monitor for increases in structured data invalid items.

- If you see an **increase in invalid items**, perhaps you rolled out a new template that doesn't work, or your site interacts with the existing template in a new and bad way.
- If you see a **decrease in valid items** (not matched by an increase in invalid items), perhaps you are no longer embedding structured data in your pages. Use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to learn what is causing the issue.

### Analyzing traffic periodically

Analyze your Google Search traffic using the [Performance Report](https://support.google.com/webmasters/answer/7576553). The data will show you how often your page appears as a rich result in Search, how often users click on it and what is the average position you appear on search results. You can also automatically pull these results with the [Search Console API](https://developers.google.com/webmaster-tools/search-console-api-original/v3/how-tos/search_analytics).

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you.

- If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
- Google does not guarantee that features that consume structured data will show up in search results. For a list of common reasons why Google may not show your content in a rich result, see the [General Structured Data Guidelines](/appearance/structured-data/sd-policies.md).
- You might have an error in your structured data. Check the [list of structured data errors](https://support.google.com/webmasters/answer/13300873) and the [Unparsable structured data report](https://support.google.com/webmasters/answer/9166415).
- If you received a structured data manual action against your page, the structured data on the page will be ignored (although the page can still appear in Google Search results). To fix [structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the [Manual Actions report](https://support.google.com/webmasters/answer/9044175).
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/recipe/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208).
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

# References & Citations

[^google-recipe]: Google Search Central (2025). "Recipe (Recipe,HowTo,ItemList) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/recipe. Retrieved 2026-09-01.
