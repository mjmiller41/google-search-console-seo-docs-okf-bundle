---
type: Reference
title: Dataset (Dataset, DataCatalog, DataDownload) structured data
description: Learn how to add schema.org dataset structured data. Implementing this can help Google recognize the dataset creator, distribution format, and other information.
resource: https://developers.google.com/search/docs/appearance/structured-data/dataset
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-14T11:36:21Z'
sources:
- id: google-dataset
  resource: https://developers.google.com/search/docs/appearance/structured-data/dataset
  title: Dataset (Dataset, DataCatalog, DataDownload) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2026-09-08T00:00:00Z'
---

# Dataset (Dataset, DataCatalog, DataDownload) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/dataset](https://developers.google.com/search/docs/appearance/structured-data/dataset). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-09-08.[^google-dataset]

Datasets are easier to find in the [Dataset Search](https://toolbox.google.com/datasetsearch/) tool when you provide supporting information such as their name, description, creator and distribution formats as structured data. Google's [approach to dataset discovery](https://www.blog.google/products/search/making-it-easier-discover-datasets/) makes use of schema.org and other metadata standards that can be added to pages that describe datasets. The purpose of this markup is to improve discovery of datasets from fields such as life sciences, social sciences, machine learning, civic and government data, and more.

![example of Dataset Search](https://developers.google.com/static/search/docs/images/dataset-search.png)

> **Note**: The actual appearance in search results might be different. You can preview most features with the [Rich Results Test](https://support.google.com/webmasters/answer/7445569).

Here are some examples of what can qualify as a dataset:

- A table or a CSV file with some data
- An organized collection of tables
- A file in a proprietary format that contains data
- A collection of files that together constitute some meaningful dataset
- A structured object with data in some other format that you might want to load into a special tool for processing
- Images capturing data
- Files relating to machine learning, such as trained parameters or neural network structure definitions

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add the [required properties](https://developers.google.com/search/docs/appearance/structured-data/dataset/#structured-data-type-definitions). Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/dataset/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Deleting a dataset from Dataset Search results

If you don't want a dataset to show up in Dataset Search results, [use the robots `meta` tag](/crawling-indexing/robots-meta-tag.md) to control how your dataset is indexed. Keep in mind that it might take some time (days or weeks, depending on the crawl schedule) for the changes to be reflected on Dataset Search.

## Our approach to dataset discovery

We can understand structured data in web pages about datasets, using either [schema.org `Dataset` markup](https://schema.org/Dataset), or equivalent structures represented in [W3C](https://www.w3.org/)'s [Data Catalog Vocabulary (DCAT) format](https://www.w3.org/TR/vocab-dcat/). We also are exploring experimental support for structured data based on [W3C CSVW](https://www.w3.org/TR/tabular-data-primer/), and expect to evolve and adapt our approach as best practices for dataset description emerge. For more information about our approach to dataset discovery, see [Making it easier to discover datasets](https://www.blog.google/products/search/making-it-easier-discover-datasets/).

## Examples

Here's an example for datasets using JSON-LD and schema.org syntax (preferred) in the Rich Results Test. The same schema.org vocabulary can also be used in RDFa 1.1 or Microdata syntaxes. You can also use the W3C DCAT vocabulary to describe the metadata. The following example is based on a [real-world dataset description](https://catalog.data.gov/dataset/ncdc-storm-events-database-336e4).

JSON-LD

Here's an example of a dataset in JSON-LD:

  

``` devsite-click-to-copy
<html>
  <head>
    <title>NCDC Storm Events Database</title>
    <script type="application/ld+json">
    {
      "@context":"https://schema.org/",
      "@type":"Dataset",
      "name":"NCDC Storm Events Database",
      "description":"Storm Data is provided by the National Weather Service (NWS) and contain statistics on...",
      "url":"https://catalog.data.gov/dataset/ncdc-storm-events-database",
      "sameAs":"https://gis.ncdc.noaa.gov/geoportal/catalog/search/resource/details.page?id=gov.noaa.ncdc:C00510",
      "identifier": ["https://doi.org/10.1000/182",
                     "https://identifiers.org/ark:/12345/fk1234"],
      "keywords":[
         "ATMOSPHERE > ATMOSPHERIC PHENOMENA > CYCLONES",
         "ATMOSPHERE > ATMOSPHERIC PHENOMENA > DROUGHT",
         "ATMOSPHERE > ATMOSPHERIC PHENOMENA > FOG",
         "ATMOSPHERE > ATMOSPHERIC PHENOMENA > FREEZE"
      ],
      "license" : "https://creativecommons.org/publicdomain/zero/1.0/",
      "isAccessibleForFree" : true,
      "hasPart" : [
        {
          "@type": "Dataset",
          "name": "Sub dataset 01",
          "description": "Informative description of the first subdataset...",
          "license" : "https://creativecommons.org/publicdomain/zero/1.0/",
          "creator":{
             "@type":"Organization",
             "name": "Sub dataset 01 creator"
          }
        },
        {
          "@type": "Dataset",
          "name": "Sub dataset 02",
          "description": "Informative description of the second subdataset...",
          "license" : "https://creativecommons.org/publicdomain/zero/1.0/",
          "creator":{
             "@type":"Organization",
             "name": "Sub dataset 02 creator"
          }
        }
      ],
      "creator":{
         "@type":"Organization",
         "url": "https://www.ncei.noaa.gov/",
         "name":"OC/NOAA/NESDIS/NCEI > National Centers for Environmental Information, NESDIS, NOAA, U.S. Department of Commerce",
         "contactPoint":{
            "@type":"ContactPoint",
            "contactType": "customer service",
            "telephone":"+1-828-271-4800",
            "email":"ncei.orders@noaa.gov"
         }
      },
      "funder":{
         "@type": "Organization",
         "sameAs": "https://ror.org/00tgqzw13",
         "name": "National Weather Service"
      },
      "includedInDataCatalog":{
         "@type":"DataCatalog",
         "name":"data.gov"
      },
      "distribution":[
         {
            "@type":"DataDownload",
            "encodingFormat":"CSV",
            "contentUrl":"https://www.ncdc.noaa.gov/stormevents/ftp.jsp"
         },
         {
            "@type":"DataDownload",
            "encodingFormat":"XML",
            "contentUrl":"https://gis.ncdc.noaa.gov/all-records/catalog/search/resource/details.page?id=gov.noaa.ncdc:C00510"
         }
      ],
      "temporalCoverage":"1950-01-01/2013-12-18",
      "spatialCoverage":{
         "@type":"Place",
         "geo":{
            "@type":"GeoShape",
            "box":"18.0 -65.0 72.0 172.0"
         }
      }
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

RDFa

Here's an example of a dataset in RDFa using the DCAT vocabulary (not supported in Rich Results Test):

``` devsite-click-to-copy
<article about="/node/1234" typeof="dcat:Dataset">
    <dl>
      <dt>Name:</dt>
      <dd property="dc:title">ACME Inc Cash flow data</dd>
      <dt>Identifiers:</dt>
      <dd property="dc:identifier">https://doi.org/10.1000/182</dd>
      <dd property="dc:identifier">https://identifiers.org/ark:/12345/fk1234</dd>
      <dt>Description:</dt>
      <dd property="dc:description">Financial Statements - Consolidated Statement of Cash Flows</dd>
      <dt>Category:</dt>
      <dd rel="dc:subject">Financial</dd>
      <dt class="field-label">Downloads:</dt>
      <dd>
        <ul>
          <li>
            <a rel="dcat:distribution" href="Consolidated_Statement_of_Cash_Flows_en.csv"><span property="dcat:mediaType" content="text/csv" >Consolidated_Statement_of_Cash_Flows_en.csv</span></a>
          </li>
         <li>
            <a rel="dcat:distribution"  href="files/Consolidated_Statement_of_Cash_Flows_en.xls"><span property="dcat:mediaType" content="application/vnd.ms-excel">Consolidated_Statement_of_Cash_Flows_en.xls</span></a>
          </li>
          <li>
            <a rel="dcat:distribution"  href="files/consolidated_statement_of_cash_flows_en.xml"><span property="dcat:mediaType" content="application/xml">consolidated_statement_of_cash_flows_en.xml</span></a>
          </li>
        </ul>
      </dd>
    </dl>
  </article>
```

## Guidelines

Sites must follow the [structured data guidelines](/appearance/structured-data/sd-policies.md). In addition to the structured data guidelines, we recommend the following [sitemap](https://developers.google.com/search/docs/appearance/structured-data/dataset/#sitemap) and [source and provenance](https://developers.google.com/search/docs/appearance/structured-data/dataset/#source-provenance) best practices.

### Sitemap best practices

Use a [sitemap file](/crawling-indexing/sitemaps/build-sitemap.md) to help Google find your URLs. Using sitemap files and `sameAs` markup helps document how dataset descriptions are published throughout your site.

If you have a dataset repository, you likely have at least two types of pages: the canonical ("landing") pages for each dataset and pages that list multiple datasets (for example, search results, or some subset of datasets). We recommend that you add structured data about a dataset to the canonical pages. Use the [`sameAs`](https://schema.org/sameAs) property to link to the canonical page if you add structured data to multiple copies of the dataset, such as listings in search results pages.

> Google doesn't need every mention of the same dataset to be explicitly marked up, but if you do so for other reasons, we strongly encourage the use of [`sameAs`](https://schema.org/sameAs).

### Source and provenance best practices

It is common for open datasets to be republished, aggregated, and to be based on other datasets. This is an initial outline of our approach to representing situations in which a dataset is a copy of, or otherwise based upon, another dataset.

- Use the [`sameAs`](https://schema.org/sameAs) property to indicate the most canonical URLs for the original in cases when the dataset or description is a simple republication of materials published elsewhere. The value of [`sameAs`](https://schema.org/sameAs) needs to unambiguously indicate the dataset's identity - in other words, don't use the same [`sameAs`](https://schema.org/sameAs) value for two different datasets.
- Use the [`isBasedOn`](https://schema.org/isBasedOn) property in cases where the republished dataset (including its metadata) has been changed significantly.
- When a dataset derives from or aggregates several originals, use the [`isBasedOn`](https://schema.org/isBasedOn) property.
- Use the [`identifier`](https://pending.webschemas.org/identifier) property to attach any relevant [Digital Object identifiers](https://en.wikipedia.org/wiki/Digital_object_identifier) (DOIs) or [Compact Identifiers](https://doi.org/10.1038/sdata.2018.29). If the dataset has more than one identifier, repeat the `identifier` property. If using JSON-LD, this is represented using JSON list syntax.

We hope to improve our recommendations based on feedback, in particular around the description of provenance, versioning, and the dates associated with time series publication. Please join in [community discussions](https://github.com/schemaorg/schemaorg/issues).

### Textual property recommendations

We recommend limiting all textual properties to 5000 characters or less. Google Dataset Search only uses the first 5000 characters of any textual property. Names and titles are typically a few words or a short sentence.

## Known Errors and Warnings

You may experience errors or warnings in Google's [Rich Results Test](https://search.google.com/test/rich-results) and other validation systems. Specifically, validation systems may suggest that organizations must have contact information including a `contactType`; useful values include `customer service`, `emergency`, `journalist`, `newsroom`, and `public engagement`. You can also ignore errors for `csvw:Table` being an unexpected value for the `mainEntity` property.

## Structured data type definitions

You must include the required properties for your content to be eligible for display as a rich result. You can also include the recommended properties to add more information about your content, which could provide a better user experience.

You can use the [Rich Results Test](https://search.google.com/test/rich-results) to validate your markup.

The focus is on describing information about a dataset (its metadata) and representing its contents. For example, dataset metadata states what the dataset is about, which variables it measures, who created it, and so on. It does not, for example, contain specific values for the variables.

### `Dataset`

The full definition of `Dataset` is available at [schema.org/Dataset](https://schema.org/Dataset).

You can describe additional information about the publication of the dataset, such as the license, when it was published, its [DOI](https://en.wikipedia.org/wiki/Digital_object_identifier), or a `sameAs` pointing to a canonical version of the dataset in a different repository. Add `identifier`, `license`, and `sameAs` for datasets that provide provenance and license information.

The Google-supported properties are the following:

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>description</code>
</td>
<td><code><a href="https://schema.org/Text">Text</a></code>
<p>A short summary describing a dataset.</p>
<p><b>Guidelines</b></p>
<ul>
<li>The summary must be between 50 and 5000 characters long.</li>
<li>The summary may include Markdown syntax. Embedded images need to use absolute path URLs
             (instead of relative paths).</li>
<li>When using the JSON-LD format, denote new lines with <code>\n</code> (two characters: backslash and lower case
             letter "n").</li>
</ul>
</td>
</tr>
<tr>
<td><code>name</code>
</td>
<td><code><a href="https://schema.org/Text">Text</a></code>
<p>A descriptive name of a dataset. For example, "Snow depth in the Northern Hemisphere".</p>
<p><b>Guidelines</b></p>
<ul>
<li>Use unique names for distinct datasets whenever possible.</li>
<p><b>Recommended</b>: <code>
               "Snow depth in the Northern Hemisphere"</code> and <code>"Snow depth in the Southern Hemisphere"</code> for two different datasets.</p>
<p><b>Not recommended</b>: <code>"Snow depth"</code> and <code>"Snow depth"</code> for two different datasets.</p>
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
<code>alternateName</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>Alternative names that have been used to refer to this dataset, such as aliases or
          abbreviations. Example (in JSON-LD format):</p>
<pre class="devsite-click-to-copy">"name": "The Quick, Draw! Dataset"
"alternateName": ["Quick Draw Dataset", "quickdraw-dataset"]</pre>
</td>
</tr>
<tr>
<td>
<code>creator</code>
</td>
<td>
<code><a href="https://schema.org/Person">Person</a></code> or
        <code><a href="https://schema.org/Organization">Organization</a></code>
<p>The creator or author of this dataset. To uniquely identify individuals, use
          <a href="https://orcid.org">ORCID ID</a> as the value of the <code>sameAs</code> property
          of the <code>Person</code> type. To uniquely identify institutions and organizations, use
          <a href="https://ror.org">ROR ID</a>.
          Example (in JSON-LD format):</p>
<pre class="devsite-click-to-copy">"creator": [
  {
    "@type": "Person",
    "sameAs": "https://orcid.org/0000-0000-0000-0000",
    "givenName": "Jane",
    "familyName": "Foo",
    "name": "Jane Foo"
  },
  {
    "@type": "Person",
    "sameAs": "https://orcid.org/0000-0000-0000-0001",
    "givenName": "Jo",
    "familyName": "Bar",
    "name": "Jo Bar"
  },
  {
    "@type": "Organization",
    "sameAs": "https://ror.org/xxxxxxxxx",
    "name": "Fictitious Research Consortium"
  }
]</pre>
</td>
</tr>
<tr>
<td><code>citation</code>
</td>
<td><code><a href="https://schema.org/Text">Text</a></code> or <code><a href="https://schema.org/CreativeWork">CreativeWork</a></code>
<p>Identifies academic articles that are recommended by the data provider be cited in addition to the
         dataset itself. Provide the citation for the dataset itself with other properties, such as <code>name</code>, <code>identifier</code>,
         <code>creator</code>, and <code>publisher</code> properties.
         For example, this property can uniquely identify a related academic publication such as a
         data descriptor, data paper, or an article for which this dataset is supplementary
         material for. Examples (in JSON-LD format):</p>
<pre class="devsite-click-to-copy">"citation": "https://doi.org/10.1111/111"</pre>
<pre class="devsite-click-to-copy">"citation": "https://identifiers.org/pubmed:11111111"</pre>
<pre class="devsite-click-to-copy">"citation": "https://identifiers.org/arxiv:0111.1111v1"</pre>
<pre class="devsite-click-to-copy">"citation":
 "Doe J (2014) Influence of X ... https://doi.org/10.1111/111"</pre>
<p><b>Additional guidelines</b></p>
<ul>
<li>Don't use this property to provide citation information for the dataset itself. It is
             intended to identify related academic articles, not the dataset itself. To provide
             information necessary to cite the dataset itself use <code>name</code>,
             <code>identifier</code>, <code>creator</code>, and <code>publisher</code> properties
             instead.</li>
<li>
             When populating the citation property with a citation snippet, provide the
             article identifier (such as a DOI) whenever possible.
             <p><b>Recommended</b>: <code> "Doe J (2014) Influence of X.
               Biomics 1(1). https://doi.org/10.1111/111"</code></p>
<p><b>Not recommended</b>: <code>"Doe J (2014) Influence of X.
               Biomics 1(1)."</code></p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<code>funder</code>
</td>
<td>
<code><a href="https://schema.org/Person">Person</a></code> or
        <code><a href="https://schema.org/Organization">Organization</a></code>
<p>A person or organization that provides financial support for this dataset. To uniquely identify individuals, use
          <a href="https://orcid.org">ORCID ID</a> as the value of the <code>sameAs</code> property
          of the <code>Person</code> type. To uniquely identify institutions and organizations, use
          <a href="https://ror.org">ROR ID</a>.
          Example (in JSON-LD format):</p>
<pre class="devsite-click-to-copy">"funder": [
  {
    "@type": "Person",
    "sameAs": "https://orcid.org/0000-0000-0000-0002",
    "givenName": "Jane",
    "familyName": "Funder",
    "name": "Jane Funder"
  },
  {
    "@type": "Organization",
    "sameAs": "https://ror.org/yyyyyyyyy",
    "name": "Fictitious Funding Organization"
  }
]</pre>
</td>
</tr>
<tr>
<td>
<code>hasPart</code> or <code>isPartOf</code>
</td>
<td><code><a href="https://schema.org/URL">URL</a></code> or
        <code><a href="https://schema.org/Dataset">Dataset</a></code>
<p>If the dataset is a collection of smaller datasets, use the <code>hasPart</code> property
          to denote such relationship. Conversly, if the dataset is part of a larger
          dataset, use <code>isPartOf</code>. Both properties can take the form of a URL
          or a <code>Dataset</code> instance. In case <code>Dataset</code> is used as a value it has
          to include all of the properties required for a standalone <code>Dataset</code>.
          Examples:</p>
<pre class="devsite-click-to-copy">"hasPart" : [
  {
    "@type": "Dataset",
    "name": "Sub dataset 01",
    "description": "Informative description of the first subdataset...",
    "license": "https://creativecommons.org/publicdomain/zero/1.0/",
    "creator": {
      "@type":"Organization",
      "name": "Sub dataset 01 creator"
    }
  },
  {
    "@type": "Dataset",
    "name": "Sub dataset 02",
    "description": "Informative description of the second subdataset...",
    "license": "https://creativecommons.org/publicdomain/zero/1.0/",
    "creator": {
      "@type":"Organization",
      "name": "Sub dataset 02 creator"
    }
  }
]</pre>
<pre class="devsite-click-to-copy">"isPartOf" : "https://example.com/aggregate_dataset"</pre>
</td>
</tr>
<tr>
<td><code>identifier</code>
</td>
<td><code><a href="https://schema.org/URL">URL</a></code>, <code><a href="https://schema.org/Text">Text</a></code>, or <code><a href="https://schema.org/PropertyValue">PropertyValue</a></code>
<p>An identifier, such as a DOI or a Compact Identifier. If the dataset has more than one
     identifier, repeat the <code>identifier</code> property. If using JSON-LD, this is represented
     using JSON list syntax.</p>
</td>
</tr>
<tr>
<td><code>isAccessibleForFree</code>
</td>
<td><code><a href="https://schema.org/Boolean">Boolean</a></code>
<p>Whether the dataset is accessible without payment.</p>
</td>
</tr>
<tr>
<td><code>keywords</code>
</td>
<td><code><a href="https://schema.org/Text">Text</a></code>
<p>Keywords summarizing the dataset.</p>
</td>
</tr>
<tr>
<td><code>license</code>
</td>
<td><code><a href="https://schema.org/URL">URL</a></code> or <code><a href="https://schema.org/CreativeWork">CreativeWork</a></code>
<p>A license under which the dataset is distributed. For example:</p>
<pre class="devsite-click-to-copy">"license" : "https://creativecommons.org/publicdomain/zero/1.0/"</pre>
<pre class="devsite-click-to-copy">"license" : {
  "@type": "CreativeWork",
  "name": "Custom license",
  "url": "https://example.com/custom_license"
  }</pre>
<p><b>Additional guidelines</b></p>
<ul>
<li>
             Provide a URL that unambiguously identifies a specific version of the license used.
             <p><b>Recommended</b></p>
<pre class="devsite-click-to-copy">"license" : "https://creativecommons.org/licenses/by/4.0"</pre>
<p><b>Not recommended</b></p>
<pre class="devsite-click-to-copy">"license" : "https://creativecommons.org/licenses/by"</pre>
</li>
</ul>
</td>
</tr>
<tr>
<td><code>measurementTechnique</code>
</td>
<td><code><a href="https://schema.org/Text">Text</a></code> or <code><a href="https://schema.org/URL">URL</a></code>
<p>The technique, technology, or methodology used in a dataset, which can correspond to the variable(s) described in <code>variableMeasured</code>.</p>
<blockquote>The <a href="https://pending.webschemas.org/measurementTechnique"><code>measurementTechnique</code></a>
          property is proposed and pending standardization at schema.org. We encourage publishers to
          share any feedback on this property with the schema.org community.</blockquote>
</td>
</tr>
<tr>
<td><code>sameAs</code>
</td>
<td><code><a href="https://schema.org/URL">URL</a></code>
<p>The URL of a reference web page that unambiguously indicates the dataset's identity.</p>
</td>
</tr>
<tr>
<td><code>spatialCoverage</code></td>
<td><code><a href="https://schema.org/Text">Text</a></code> or <code><a href="https://schema.org/Place">Place</a></code>
<p>You can provide a single point that describes the spatial aspect of the dataset. Only
         include this property if the dataset has a spatial dimension. For example,
         a single point where all the measurements were collected, or the coordinates of a bounding
         box for an area.</p>
<p><b>Points</b></p>
<pre class="devsite-click-to-copy">"spatialCoverage:" {
  "@type": "Place",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 39.3280,
    "longitude": 120.1633
  }
}</pre>
<p><b>Shapes</b></p>
<p>Use <a href="https://schema.org/GeoShape"><code>GeoShape</code></a> to describe areas of different shapes. For example, to specify a bounding box.</p>
<pre class="devsite-click-to-copy">"spatialCoverage:" {
  "@type": "Place",
  "geo": {
    "@type": "GeoShape",
    "box": "39.3280 120.1633 40.445 123.7878"
  }
}</pre>
<p><b>Points inside <code>box</code>, <code>circle</code>, <code>line</code>, or
         <code>polygon</code> properties must be expressed as a space separated pair of two
         values corresponding to latitude and longitude (in that order).</b>
</p>
<p><b>Named locations</b></p>
<pre class="devsite-click-to-copy">"spatialCoverage:" "Tahoe City, CA"</pre>
</td>
</tr>
<tr>
<td><code>temporalCoverage</code></td>
<td><code><a href="https://schema.org/Text">Text</a></code>
<p>The data in the dataset covers a specific time interval. Only include this property if the
         dataset has a temporal dimension. Schema.org uses the ISO 8601 standard
         to describe time intervals and time points. You can describe dates differently depending
         upon the dataset interval. Indicate open-ended intervals with two decimal points (<code>..</code>).

       <p><b>Single date</b></p>
<pre class="devsite-click-to-copy">"temporalCoverage" : "2008"</pre>
<p><b>Time period</b></p>
<pre class="devsite-click-to-copy">"temporalCoverage" : "1950-01-01/2013-12-18"</pre>
<p><b>Open-ended time period</b></p>
<pre class="devsite-click-to-copy">"temporalCoverage" : "2013-12-19/.."</pre>
</p></td>
</tr>
<tr>
<td><code>variableMeasured</code>
</td>
<td><code><a href="https://schema.org/Text">Text</a></code> or <code><a href="https://schema.org/PropertyValue">PropertyValue</a></code>
<p>The variable that this dataset measures. For example, temperature or pressure.</p>
<blockquote>The <a href="https://pending.webschemas.org/variableMeasured"><code>variableMeasured</code></a>
          property is proposed and pending standardization at schema.org. We encourage publishers to
          share any feedback on this property with the schema.org community.</blockquote>
</td>
</tr>
<tr>
<td><code>version</code>
</td>
<td><code><a href="https://schema.org/Text">Text</a></code> or <code><a href="https://schema.org/Number">Number</a></code>
<p>The version number for the dataset.</p>
</td>
</tr>
<tr>
<td><code>url</code>
</td>
<td><code><a href="https://schema.org/URL">URL</a></code>
<p>Location of a page describing the dataset.</p>
</td>
</tr>
</tbody>
</table>

### `DataCatalog`

The full definition of `DataCatalog` is available at [schema.org/DataCatalog](https://schema.org/DataCatalog).

Datasets are often published in repositories that contain many other datasets. The same dataset can be included in more than one such repository. You can refer to a data catalog that this dataset belongs to by referencing it directly by using the following properties:

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Recommended properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>includedInDataCatalog</code>
</td>
<td><code><a href="https://schema.org/DataCatalog">DataCatalog</a></code>
<p>
   The catalog to which the dataset belongs.<p>
</p></p></td>
</tr>
</tbody>
</table>

### `DataDownload`

The full definition of `DataDownload` is available at [schema.org/DataDownload](https://schema.org/DataDownload). In addition to Dataset properties, add the following properties for datasets that provide download options.

The `distribution` property describes how to get the dataset itself because the URL often points to the landing page describing the dataset. The `distribution` property describes where to get the data and in what format. This property can have several values: for instance, a CSV version has one URL and an Excel version is available at another.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>distribution.contentUrl</code>
</td>
<td><code><a href="https://schema.org/URL">URL</a></code>
<p>
   The link for the download.</p>
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
<td><code>distribution</code>
</td>
<td><code><a href="https://schema.org/DataDownload">DataDownload</a></code>
<p>The description of the location for download of the dataset and the file format for
   download.<p>
</p></p></td>
</tr>
<tr>
<td><code>distribution.encodingFormat</code>
</td>
<td><code><a href="https://schema.org/Text">Text</a></code> or <code><a href="https://schema.org/URL">URL</a></code>
<p>
         The file format of the distribution.<p>
</p></p></td>
</tr>
</tbody>
</table>

### Tabular datasets

> **Beta**: This approach is currently in beta and therefore subject to change.

A [tabular dataset](https://www.w3.org/TR/tabular-data-model/#intro) is one organized primarily in terms of a grid of rows and columns. For pages that embed tabular datasets, you can also create more explicit markup, building on the [basic approach](https://developers.google.com/search/docs/appearance/structured-data/dataset/#approach). At this time we understand a variation of CSVW ("CSV on the Web", see [W3C](https://www.w3.org/2013/csvw/wiki/Main_Page)), provided in parallel to user-oriented tabular content on the HTML page.

Here is an example showing a small table encoded in CSVW JSON-LD format. There are some [known errors](https://developers.google.com/search/docs/appearance/structured-data/dataset/#knownerrors) in the Rich Results Test.

  

``` devsite-click-to-copy
<html>
  <head>
    <title>American Humane Association</title>
    <script type="application/ld+json">
    {
      "@context": ["https://schema.org", {"csvw": "https://www.w3.org/ns/csvw#"}],
      "@type": "Dataset",
      "name":"AMERICAN HUMANE ASSOCIATION",
      "description": "ProPublica's Nonprofit Explorer lets you view summaries of 2.2 million tax returns from tax-exempt organizations and see financial details such as their executive compensation and revenue and expenses. You can browse raw IRS data released since 2013 and access over 9.4 million tax filing documents going back as far as 2001.",
      "publisher": {
        "@type": "Organization",
        "name": "ProPublica"
      },
      "mainEntity" : {
        "@type" : "csvw:Table",
        "csvw:tableSchema": {
          "csvw:columns": [
            {
              "csvw:name": "Year",
              "csvw:datatype": "string",
              "csvw:cells": [
                {
                  "csvw:value": "2024",
                  "csvw:primaryKey": "2024"
                },
                {
                  "csvw:value": "2024",
                  "csvw:primaryKey": "2024"
                }]
            },
            {
              "csvw:name": "Organization name",
              "csvw:datatype": "string",
              "csvw:cells": [
                {
                  "csvw:value": "AMERICAN HUMANE ASSOCIATION",
                  "csvw:primaryKey": "2024"
                },
                {
                  "csvw:value": "AMERICAN HUMANE ASSOCIATION",
                  "csvw:primaryKey": "2024"
                }]
            },
            {
              "csvw:name": "Organization address",
              "csvw:datatype": "string",
              "csvw:cells": [
                {
                  "csvw:value": "1400 16TH STREET NW",
                  "csvw:primaryKey": "2024"
                },
                {
                  "csvw:value": "1400 16TH STREET NW",
                  "csvw:primaryKey": "2024"
                }]
            },
            {
              "csvw:name": "Organization NTEE Code",
              "csvw:datatype": "string",
              "csvw:cells": [
                {
                  "csvw:value": "D200",
                  "csvw:notes": "Animal Protection and Welfare",
                  "csvw:primaryKey": "2024"
                },
                {
                  "csvw:value": "D200",
                  "csvw:notes": "Animal Protection and Welfare",
                  "csvw:primaryKey": "2024"
                }]
            },
            {
              "csvw:name": "Total functional expenses ($)",
              "csvw:datatype": "integer",
              "csvw:cells": [
                {
                  "csvw:value": "13800212",
                  "csvw:primaryKey": "2024"
                },
                {
                  "csvw:value": "13800212",
                  "csvw:primaryKey": "2024"
                }]
            }]
        }
      }
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

## Monitor rich results with Search Console

Search Console is a tool that helps you monitor how your pages perform in Google Search. You don't have to sign up for Search Console to be included in Google Search results, but it can help you understand and improve how Google sees your site. We recommend checking Search Console in the following cases:

1.  [After deploying structured data for the first time](https://developers.google.com/search/docs/appearance/structured-data/dataset/#after-deploying)
2.  [After releasing new templates or updating your code](https://developers.google.com/search/docs/appearance/structured-data/dataset/#after-releasing)
3.  [Analyzing traffic periodically](https://developers.google.com/search/docs/appearance/structured-data/dataset/#analyzing-periodically)

### After deploying structured data for the first time

After Google has indexed your pages, look for issues using the relevant [Rich result status report](https://support.google.com/webmasters/answer/7552505). Ideally, there will be an increase of valid items, and no increase in invalid items. If you find issues in your structured data:

1.  [Fix the invalid items](https://developers.google.com/search/docs/appearance/structured-data/dataset/#troubleshooting).
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
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/dataset/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- Structured data issues can affect how your site's content appears in search results. Use this [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208) guide to review a step-by-step approach to identify, fix, and validate these issues in Search Console.
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

### Specific dataset isn't showing up in Dataset Search results

*error* **What caused the issue**: Your site doesn't have structured data on the page that describes the datasets or the page hasn't been crawled yet.

*done* **Fix the issue**

1.  Copy the link for the page that you expect to see in Dataset Search results, and put it into the [Rich Results Test](https://search.google.com/test/rich-results). If the message "Page not eligible for rich results known by this test" or "Not all markup is eligible for rich results" appears, this means there's no dataset markup on the page or it's incorrect. You can fix it by referring to the [How to add structured data](https://developers.google.com/search/docs/appearance/structured-data/dataset/#add-structured-data) section.
2.  If there is markup on the page, it may not have been crawled yet. You can [check the crawl status](https://support.google.com/webmasters/answer/7440203) with Search Console.

### Company logo is missing or not appearing correctly by results

*error* **What caused the issue**: Your page may be missing schema.org markup for organization logos or your business isn't established with Google.

*done* **Fix the issue**

1.  Add [logo structured data](/appearance/structured-data/organization.md) to your page.
2.  [Establish your business details](/appearance/establish-business-details.md) with Google.

# References & Citations

[^google-dataset]: Google Search Central (2026). "Dataset (Dataset, DataCatalog, DataDownload) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/dataset. Retrieved 2026-09-14.
