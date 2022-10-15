# My personal website
-- Created with [Quarto](https://quarto.org) --

-- Published with [GitHub Pages](https://pages.github.com/) --

-- Learned from the tutorials of [Quarto](https://quarto.org) and of [Albert Rapp](https://albert-rapp.de/posts/13_quarto_blog_writing_guide/13_quarto_blog_writing_guide) --

### Quarto v1.1.251 Linux release

I modified one script in their package to fixed the issue with code tools & external links.

- File: `share/formats/html/templates/quarto-html.ejs`

- Line #220-221:

  ```javascript
  // window.location.href = sourceUrl;
  window.open(sourceUrl, '_blank'); // always open source code URL in new window
  ```

- Line #345-346:

  ```javascript
  // Inspect non-navigation links and adorn them if external
  var links = window.document.querySelectorAll('a:not(.nav-link):not(.navbar-brand):not(.toc-action):not(.sidebar-link):not(.sidebar-item-toggle):not(.pagination-link):not(.no-external):not(.dropdown-item)');
  ```

