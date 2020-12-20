# Contributing

You can contribute Scrolls or to the library itself.

The library is a currently client side only, static Vue.js website. A proper backend with a Scroll
database and user management will be added at some point.

In the meantime Scrolls live in the [`public/scrolls`](public/scrolls) directory.

## Scroll Development

There is/will be a guide on the library website.

### Types of Scrolls

- CSS: Themes, widgets and page templates
- User Scripts
- Text Templates: RemNote templates and literal text templates

### Add an existing repo as a scroll

After you cloned the library, add the repository as a submodule:

```sh
cd ~/path/to/remnote-library
git submodule add https://github.com/user/your-repo.git public/scrolls/your-repo
```

Then create a `manifest.json` and fill in the required information:

```sh
cp scroll-templates/custom-css/manifest.json public/scrolls/your-repo
cd public/scrolls/your-repo
vim manifest.json
```

See [`manifest.schema.json`](manifest.schema.json) for a description of the required fields.

**TODO:** Make a proper guide.

#### CSS

- Widgets: Change the display of a rem (and its children) with a tag
  - Table, Column layout
  - Math environments
- Themes: Change the Look&Feel of the whole application.
- Page Templates: Have a document displayed in a certain way
  - Meeting notes
  - Weekly plan, Calendar View
  - Digital Gardens, Knowledge Maps, Structure Zettel

Install methods:

- copy
- api (later)

- Best practice is to have the copied block consisting of a `:root {}` block with variables the user can customize and one or more `@import`s
  - TODO: How are `@import`s handled when offline?
- Have semver version `major.minor[.patch]`
  - `major` do not update correctly automatically. They have to be recopied&pasted, e.g. major `:root` changes.
  - `minor`/`patch` a change that the user does not have to act on.

#### User Scripts

- Installed via Violentmonkey, Tampermonkey.
- Lightweight

### Install methods

- Copy: Something is copied to clipboard. Depending on the package type the user should paste it somewhere
  - A CSS/Theme package should be pasted in a block on the Custom CSS page.

## Library Development

Some Scrolls are added as git submodules. This means you have to clone (your fork) with

```sh
git clone --recurse-submodules https://github.com/hannesfrank/remnote-library.git
# Or if you already cloned, update the submodules
git submodule update --init --recursive
```

All development tasks can be found in `package.json:scripts`.

Install dependencies:

```
yarn install
```

### Compiles and hot-reloads for development

Live-reload the library:

```sh
yarn serve
```

You might have to go to `https://YOUR_IP:8080` instead of `https://localhost:8080` for the live reload to work.

Live-reload the scroll database:

```sh
yarn watch-scrolls
```

### Release

There is a Github workflow which automatically builds and deploys the project when commits are added to the master branch.
