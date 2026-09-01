---
type: Reference
title: Math solver (MathSolver) structured data
description: Learn how to add math solver structured data to ensure users are connecting with learning resources that are relevant in Google Search results.
resource: https://developers.google.com/search/docs/appearance/structured-data/math-solvers
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-math-solvers
  resource: https://developers.google.com/search/docs/appearance/structured-data/math-solvers
  title: Math solver (MathSolver) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-18T00:00:00Z'
---

# Math solver (MathSolver) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/math-solvers](https://developers.google.com/search/docs/appearance/structured-data/math-solvers). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-18.[^google-math-solvers]

To help students, teachers, and others with math problems, you can use structured data to indicate the type of math problems and links to step-by-step walkthroughs for specific math problems. Here's an example of how math solvers may look in Google Search results (the appearance is subject to change):

![Example of a math solvers rich result](https://developers.google.com/static/search/docs/images/math-solvers-rich-result.png)

> **Note**: The actual appearance in search results might be different. You can preview most features with the [Rich Results Test](https://support.google.com/webmasters/answer/7445569).

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add the [required properties](https://developers.google.com/search/docs/appearance/structured-data/math-solvers/#structured-data-type-definitions). Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/math-solvers/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Examples

### One solver action

Here's an example of a math solver home page that has one solver action that can solve polynomial equations and derivative problems and is available in English and Spanish.

  

``` devsite-click-to-copy
<html>
<head>
<title>An awesome math solver</title>
</head>
<body>
<script type="application/ld+json">
[
  {
    "@context": "https://schema.org",
    "@type": ["MathSolver", "LearningResource"],
    "name": "An awesome math solver",
    "url": "https://www.mathdomain.com/",
    "usageInfo": "https://www.mathdomain.com/privacy",
    "inLanguage": "en",
    "potentialAction": [{
      "@type": "SolveMathAction",
      "target": "https://mathdomain.com/solve?q={math_expression_string}",
      "mathExpression-input": "required name=math_expression_string",
      "eduQuestionType": ["Polynomial Equation","Derivative"]
     }],
    "learningResourceType": "Math solver"
  },
  {
    "@context": "https://schema.org",
    "@type": ["MathSolver", "LearningResource"],
    "name": "Un solucionador de matemáticas increíble",
    "url": "https://es.mathdomain.com/",
    "usageInfo": "https://es.mathdomain.com/privacy",
    "inLanguage": "es",
    "potentialAction": [{
      "@type": "SolveMathAction",
      "target": "https://es.mathdomain.com/solve?q={math_expression_string}",
      "mathExpression-input": "required name=math_expression_string",
      "eduQuestionType": ["Polynomial Equation","Derivative"]
     }],
    "learningResourceType": "Math solver"
  }
]
</script>
</body>
</html>
```

> The Spanish markup could be placed directly on `https://es.mathdomain.com/` instead of placing it alongside the English version of the math solver markup.

### Two solver actions

Here's an example of a math solver home page that has two solver endpoints: one endpoint can solve polynomial equations and the other endpoint can solve trigonometric equations. It is available only in English.

  

``` devsite-click-to-copy
<html>
<head>
<title>An awesome math solver</title>
</head>
<body>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["MathSolver", "LearningResource"],
  "name": "An awesome math solver",
  "url": "https://www.mathdomain.com/",
  "usageInfo": "https://www.mathdomain.com/privacy",
  "inLanguage": "en",
  "potentialAction": [{
     "@type": "SolveMathAction",
     "target": "https://mathdomain.com/solve?q={math_expression_string}",
     "mathExpression-input": "required name=math_expression_string",
     "eduQuestionType": "Polynomial Equation"
   },
   {
     "@type": "SolveMathAction",
     "target": "https://mathdomain.com/trig?q={math_expression_string}",
     "mathExpression-input": "required name=math_expression_string",
     "eduQuestionType": "Trigonometric Equation"
   }],
  "learningResourceType": "Math solver"
}
</script>
</body>
</html>
```

## Guidelines

For your page to be eligible for math solver rich results, you must follow these guidelines:

- [General structured data guidelines](/appearance/structured-data/sd-policies.md)
- [Search Essentials](/essentials/overview.md)
- [Technical guidelines](https://developers.google.com/search/docs/appearance/structured-data/math-solvers/#technical-guidelines)
- [Content guidelines](https://developers.google.com/search/docs/appearance/structured-data/math-solvers/#content-guidelines)

### Technical Guidelines

- Add `MathSolver` structured data to the home page of your site.
- Ensure that Googlebot can [crawl your site efficiently](/crawling-indexing/troubleshoot-crawling-errors.md).
- If you have several identical copies of the same math solver hosted under different URLs, use the [canonical URLs](/crawling-indexing/consolidate-duplicate-urls.md) on each copy of the page.
- We don't allow math solvers that are entirely hidden behind a login or paywall. Once users navigate from the feature on Google to your site, the solution and a step-by-step walkthrough for their initial problem must be accessible to them. Additional content can be behind a login or paywall.

### Content guidelines

We created these Math Solver content guidelines to ensure that our users are connected with learning resources that are relevant. If we find content that violates these policies, we'll respond appropriately, which may include taking [manual action](https://support.google.com/webmasters/answer/9044175) and removing your pages from appearing in the math solver experience on Google.

- We don't allow promotional content disguised as a math solver, such as those posted by a third party (for example, [affiliate programs](/essentials/spam-policies.md)).
- You are responsible for the accuracy and quality of your math solver through this feature. If a certain amount of your data is found to be inaccurate based on our quality review processes, then your solver may be removed from the feature until you resolve the issues depending on the severity. This applies to:
  - The accuracy of the problem types your solver is capable of solving.
  - The accuracy of your solutions for math problems your solver declares it can solve.

## Structured data type definitions

You must include the required properties for your content to be eligible for display as a rich result. You can also include the recommended properties to add more information to your structured data, which could provide a better user experience.

### MathSolver

A `MathSolver` is a tool that assists students, teachers, and others with math problems by laying out step-by-step solutions. Use `MathSolver` structured data on your site's home page.

The full definition of `MathSolver` is available at [schema.org/MathSolver](https://schema.org/MathSolver).

The Google-supported properties are the following:

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>potentialAction</code></td>
<td><p><code><a href="https://schema.org/SolveMathAction">SolveMathAction</a></code></p>
<p>The action that leads to a mathematical explanation (for example, step-by-step solution or graph) of a math expression.</p>
<pre class="devsite-click-to-copy">{
"@type": "MathSolver",
"potentialAction": [{
  "@type": "SolveMathAction",
  "target": "https://mathdomain.com/solve?q={math_expression_string}",
  "mathExpression-input": "required name=math_expression_string",
  "eduQuestionType": "Polynomial Equation"
  }]
}</pre>
</td>
</tr>
<tr>
<td><code>potentialAction.mathExpression-input</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>
          A placeholder for a mathematical expression (for example: x^2-3x=0) that is sent by Google
          to your website. You can then "solve" the math expression, which may involve simplifying,
          transforming, or solving for a specific variable. The string can take many formats
          (for example: LaTeX, Ascii-Math, or mathematical expressions that you can write with a
          keyboard).
        </p>
<blockquote>
<code>mathExpression-input</code> is an annotated property. See the
          <a href="https://schema.org/docs/actions.html#part-4"><code>Potential Actions</code></a>
          page for more information.
        </blockquote>
<p>For some problem types, the <code>math_expression_string</code> indicates both the problem type and
          parameters of the problem type. Here are some examples of the more complicated problem
          types so that you can anticipate and parse them correctly.
        </p>
<p><b>Derivatives</b></p>
<p>Google will send a <code>math_expression_string</code> in one of two forms:</p>
<ul>
<li><pre class="devsite-click-to-copy">(<var>math_expression</var>)'</pre></li>
 <li><pre class="prettyprint">d/d<var>variable</var> <var>math_expression</var></pre></li>
 </ul>
 <p>Examples:</p>
 <ul>
 <li><code>(x^2+x)'</code></li>
 <li><code>d/dx (x^2+x)</code></li>
 <li><code>d/dy y^2+y</code></li>
 </ul>
 <p><b>Integrals</b></p>
 <p>Google will send a <code>math_expression_string</code> in one of two forms:</p>
 <ul>
 <li><pre class="prettyprint">\int <var>math_expression</var></pre></li>
<li><pre class="devsite-click-to-copy">\int_{<var>from</var>}^{<var>to</var>} <var>math_expression</var></pre></li>
</ul>
<p>Examples:</p>
<ul>
<li><code>\int x^2+x</code></li>
<li><code>\int_{0}^{2} x^2+x</code></li>
</ul>
<p><b>Limits</b></p>
<p>Google will send a <code>math_expression_string</code> in one of two forms:</p>
<ul>
<li><pre class="devsite-click-to-copy">\lim <var>math_expression</var></pre></li>
<li><pre class="devsite-click-to-copy">\lim_{<var>variable</var>\rightarrow<var>value</var>} <var>math_expression</var></pre></li>
</ul>
<p>Examples:</p>
<ul>
<li><code>\lim_{x\rightarrow0} sin(x)/x</code></li>
<li><code>\lim_{y\rightarrow\infty} sin(y)/y</code></li>
<li><code>\lim sin(x)/x</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>url</code></td>
<td><p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>The URL of the <code>MathSolver</code>.</p></td>
</tr>
<tr>
<td><code>usageInfo</code></td>
<td><p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>The privacy policy for your math problem solving site.</p>
<pre class="devsite-click-to-copy devsite-code-highlight">{
  "@type": "MathSolver",
  <strong>"usageInfo": "https://www.mathdomain.com/privacy"</strong>
}</pre></td>
</tr>
<tr>
<td><code>potentialAction.target</code></td>
<td><p><code><a href="https://schema.org/EntryPoint">EntryPoint</a></code></p>
<p>The URL target entrypoint for an action. The <code>potentialAction.target</code>
          property accepts a string to represent the math expression that's being solved by the action.</p>
<pre class="devsite-click-to-copy devsite-code-highlight">{
"@type": "MathSolver",
"potentialAction": [{
  "@type": "SolveMathAction",
  <strong>"target": "https://mathdomain.com/solve?q={math_expression_string}"</strong>
  }]
}</pre>
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
<td><code>inLanguage</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The language(s) that are supported by your math problem solving site. See <a href="https://developers.google.com/custom-search/docs/xml_results_appendices#interfaceLanguages">this table</a>
          for a list of possible languages.</p>
<pre class="devsite-click-to-copy devsite-code-highlight">{
  "@type": "MathSolver",
  <strong>"inLanguage": "es"</strong>
}</pre></td>
</tr>
<tr>
<td><code>assesses</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code>
        list of <a href="https://developers.google.com/search/docs/appearance/structured-data/math-solvers/#problem-type-definitions">Problem Type Definitions</a></p>
<p>The problem type(s) that are solved with the <code>HowTo</code>. Use the
          <code>assesses</code> property if you're using <code>HowTo</code>
          markup in addition to <code>MathSolver</code> markup.</p>
<pre class="devsite-click-to-copy devsite-code-highlight">{
  "@type": "MathSolver",
  <strong>"assesses": "Polynomial Equation"</strong>
}</pre></td>
</tr>
<tr>
<td><code>potentialAction.eduQuestionType</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code>
        list of <a href="https://developers.google.com/search/docs/appearance/structured-data/math-solvers/#problem-type-definitions">Problem Type Definitions</a></p>
<p>The problem type(s) that are capable of being solved by the <code>potentialAction.target</code> property.</p>
<pre class="devsite-click-to-copy devsite-code-highlight">{
  "@type": "SolveMathAction",
  <strong>"eduQuestionType": "Polynomial Equation"</strong>
}</pre></td>
</tr>
</tbody>
</table>

### LearningResource

A `LearningResource` indicates that the subject of the markup is a resource that assists students, teachers, and others with educational learning. Use `LearningResource` on your site's home page.

The full definition of `LearningResource` is available at [schema.org/LearningResource](https://schema.org/LearningResource).

The Google-supported properties are the following:

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>learningResourceType</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The type of this learning resource. Use this fixed value: <code>Math Solver</code>.</p>
<pre class="devsite-click-to-copy devsite-code-highlight">{
  "@type": ["MathSolver", "LearningResource"],
  <strong>"learningResourceType": "Math Solver"</strong>
}</pre>
</td>
</tr>
</tbody>
</table>

## Problem Type Definitions

Use the following list of problem types as either the `eduQuestionType` for a `MathSolver.potentialAction` or for the `assesses` field of a `MathSolver` when the `MathSolver` is accompanying a `HowTo` that walks through a specific math problem.

The following table shows some examples for the problem types you can annotate:

<table>
<tr>
<th colspan="2">Example problem types (this isn't an exhaustive list)</th>
</tr>
<tr>
<td><code>Absolute Value Equation</code></td>
<td><p>Absolute value equations. For example: |x - 5| = 9</p></td>
</tr>
<tr>
<td><code>Algebra</code></td>
<td><p>A generic problem type that can be placed with other problem type. For example: polynomial equations, exponential equations, and radical expressions.</p></td>
</tr>
<tr>
<td><code>Arc Length</code></td>
<td><p>Arc length problems. For example: Determine the length of x = 4 (3 + y)^2, 1 &lt; y &lt; 4.</p></td>
</tr>
<tr>
<td><code>Arithmetic</code></td>
<td><p>Arithmetic problems. For example: Find the sum of 5 + 7.</p></td>
</tr>
<tr>
<td><code>Biquadratic Equation</code></td>
<td><p>Biquadratic equations. For example: x^4 - x^2 - 2 = 0.</p></td>
</tr>
<tr>
<td><code>Calculus</code></td>
<td><p>A generic problem type that can be placed with other problem types. For example: integrals, derivatives, and differential equations.</p></td>
</tr>
<tr>
<td><code>Characteristic Polynomial</code></td>
<td><p>Find the characteristic polynomial of {{1,2,5}, {3,-1,1}, {1,2,3}}.</p></td>
</tr>
<tr>
<td><code>Circle</code></td>
<td><p>Circle related problems. For example: Find the radius of x^2 + y^2 = 3.</p></td>
</tr>
<tr>
<td><code>Derivative</code></td>
<td><p>Derivative of 5x^4 + 2x^3 + 4x - 2.</p></td>
</tr>
<tr>
<td><code>Differential Equation</code></td>
<td><p>Differential equation problems. For example: y+dy/dx=5x.</p></td>
</tr>
<tr>
<td><code>Distance</code></td>
<td><p>Distance problems. For example: Find the distance between (6,-1) and (-3,2).</p></td>
</tr>
<tr>
<td><code>Eigenvalue</code></td>
<td><p>Eigenvalue problems. For example: Find the eigenvalues for the matrix [[-6, 3], [4, 5]].</p></td>
</tr>
<tr>
<td><code>Eigenvector</code></td>
<td><p>Eigenvector problems. For example: Find the eigenvector for the matrix [[-6, 3], [4, 5]] with eigenvalues of [-7, 6].</p></td>
</tr>
<tr>
<td><code>Ellipse</code></td>
<td><p>Ellipse problems. For example: Find the x and y intercepts of 9x^2 + 4y^2 = 36.</p></td>
</tr>
<tr>
<td><code>Exponential Equation</code></td>
<td><p>Exponential equations. For example: 7^x = 9.</p></td>
</tr>
<tr>
<td><code>Function</code></td>
<td><p>Polynomial simplifications. For example: (x-5)^2 * (x+5)^2.</p></td>
</tr>
<tr>
<td><code>Function Composition</code></td>
<td><p>f(g(x)) when f(x)=x^2-2x, g(x)=2x-2</p></td>
</tr>
<tr>
<td><code>Geometry</code></td>
<td><p>A generic problem type that can be placed with other problem types. For example: circle, ellipse, parabola, slope.</p></td>
</tr>
<tr>
<td><code>Hyperbola</code></td>
<td><p>Hyperbola problems. For example: Find the x-intercept of (x^2)/4 - (y^2)/5 = 1.</p></td>
</tr>
<tr>
<td><code>Inflection Point</code></td>
<td><p>Find the inflection point of f(x) = 1/2x^4 +x^3 - 6x^2.</p></td>
</tr>
<tr>
<td><code>Integral</code></td>
<td><p>Integral of sqrt (x^2 - y^2).</p></td>
</tr>
<tr>
<td><code>Intercept</code></td>
<td><p>Line intercept problems. For example: Find the x-intercept of the line y = 10x - 5.</p></td>
</tr>
<tr>
<td><code>Limit</code></td>
<td><p>Limit problems. For example: Find the limit of x as x approaches 1 for (x^2-1)/(x-1).</p></td>
</tr>
<tr>
<td><code>Line Equation</code></td>
<td><p>Line equation problems. For example: Find the equation of a line with points (-7,-4) and (-2,-6).</p></td>
</tr>
<tr>
<td><code>Linear Algebra</code></td>
<td><p>A generic problem type that can be placed with other problem types. For example: matrix and characteristic polynomial.</p></td>
</tr>
<tr>
<td><code>Linear Equation</code></td>
<td><p>Linear equations. For example: 4x - 3 = 2x + 9.</p></td>
</tr>
<tr>
<td><code>Linear Inequality</code></td>
<td><p>Linear inequalities. For example: 5x - 6 &gt; 3x - 8.</p></td>
</tr>
<tr>
<td><code>Logarithmic Equation</code></td>
<td><p>Logarithmic equations. For example: log(x) = log(100).</p></td>
</tr>
<tr>
<td><code>Logarithmic Inequality</code></td>
<td><p>Logarithmic inequalities. For example: log(x) &gt; log(100).</p></td>
</tr>
<tr>
<td><code>Matrix</code></td>
<td><p>{{1,2,5}, {3,-1,1}, {1,2,3}} row reduce</p></td>
</tr>
<tr>
<td><code>Midpoint</code></td>
<td><p>Midpoint problems. For example: find the midpoint between (-3, 7) and (5, -2).</p></td>
</tr>
<tr>
<td><code>Parabola</code></td>
<td><p>Parabola problems. For example: Find the vertex of y2 - 4x - 4y = 0.</p></td>
</tr>
<tr>
<td><code>Parallel</code></td>
<td><p>Parallel line problems. For example: Are the two lines parallel (y = 10x + 5, y = 20x + 10)?</p></td>
</tr>
<tr>
<td><code>Perpendicular</code></td>
<td><p>Perpendicular problems. For example: Are the two lines perpendicular (y = 10x + 5, y = 20x + 10)?</p></td>
</tr>
<tr>
<td><code>Polynomial Equation</code></td>
<td><p>Polynomial equations. For example: x^5 - 3x = 0.</p></td>
</tr>
<tr>
<td><code>Polynomial Expression</code></td>
<td><p>Polynomial expressions. For example: (x - 5)^4 * (x + 5)^2.</p></td>
</tr>
<tr>
<td><code>Polynomial Inequality</code></td>
<td><p>Polynomial inequalities. For example: x^4 - x^2 - 6 &gt; x^3 - 3x^2.</p></td>
</tr>
<tr>
<td><code>Quadratic Equation</code></td>
<td><p>Quadratic equations. For example: x^2 - 3x - 4 = 0.</p></td>
</tr>
<tr>
<td><code>Quadratic Expression</code></td>
<td><p>Quadratic expressions. For example: x^2 - 3x - 2.</p></td>
</tr>
<tr>
<td><code>Quadratic Inequality</code></td>
<td><p>Quadratic inequalities. For example: x^2 - x - 6 &gt; x^2 - 3x.</p></td>
</tr>
<tr>
<td><code>Radical Equation</code></td>
<td><p>Radical equations. For example: sqrt(x) - x = 0.</p></td>
</tr>
<tr>
<td><code>Radical Inequality</code></td>
<td><p>Radical inequalities. For example: sqrt(x) - x &gt; 0.</p></td>
</tr>
<tr>
<td><code>Rational Equation</code></td>
<td><p>Rational equations. For example: 5/(x - 3) = 2/(x - 1).</p></td>
</tr>
<tr>
<td><code>Rational Expression</code></td>
<td><p>Rational expressions. For example: 1/(x^3 + 4x^2 + 5x + 2).</p></td>
</tr>
<tr>
<td><code>Rational Inequality</code></td>
<td><p>Rational inequalities. For example: 5/(x - 3) &gt; 2/(x - 1).</p></td>
</tr>
<tr>
<td><code>Slope</code></td>
<td><p>Slope problems. For example: Find the slope of y = 10x + 5.</p></td>
</tr>
<tr>
<td><code>Statistics</code></td>
<td><p>Statistics problems. For example: Find the mean of a set of numbers (3, 8, 2, 10).</p></td>
</tr>
<tr>
<td><code>System of Equations</code></td>
<td><p>System of equations problems. For example: Solve 2x + 5y = 16;3x - 5y = - 1.</p></td>
</tr>
<tr>
<td><code>Trigonometry</code></td>
<td><p>Solve sin(t) + cos(t) = 1.</p></td>
</tr>
</table>

# References & Citations

[^google-math-solvers]: Google Search Central (2025). "Math solver (MathSolver) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/math-solvers. Retrieved 2026-09-01.
