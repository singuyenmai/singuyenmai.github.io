### Quarto v1.1.251 Linux release

I modified one script in their package to fix the issue with code tools & external links.

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

### Quarto v1.3.302 MacOS release

- Navbar background color is no longer assigned by `$primary`, but by `$navbar-bg`
- Fixed bug [#5067](https://github.com/quarto-dev/quarto-cli/issues/5067) according to commit [0445941](https://github.com/quarto-dev/quarto-cli/commit/0445941eafff77812312456d8a6bd4667259e680)