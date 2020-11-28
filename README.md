# remnote-library

## Package Development

TODO: Publish this guide on the website.

### Types of packages

- CSS: Themes, widgets and page templates
- User Scripts
- Text Templates: RemNote templates and literal text templates

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

This is just a (currently client side only) website.

### Libarry
```
yarn install
```

#### Compiles and hot-reloads for development
```
yarn serve
```
You might have to go to `https://YOUR_ID:8080` instead of `https://localhost:8080` for the live reload to work.

#### Compiles and minifies for production
```
yarn build
```

#### Lints and fixes files
```
yarn lint
```
