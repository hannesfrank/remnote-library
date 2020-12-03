# Development Notes

## LiveReload Approaches

I brainstormed multiple things that could work. So far Option 3 works and is documented above.

- Option 1: Edit styles manually in RemNote
  - Problem: Have to copy styles to editor afterwards
  - Problem: Scroll to view code and elements
  - Problem: Bad editing experience
- Option 2: LiveServer
  - How can I do this?
  - Use this `@import URL('http://127.0.0.1:5500/test.css');` in RemNote.
    - It does not reload automatically, only when the checkmark is toggeled or the code is edited.
      - I could write an extension which toggles the checkbox with `setInterval`.
  - Try adding a LiveReload script manually as a script tag.
  - Use a live-reload browser extension.
- Option 3: Persist DevTools edits [StackOverflow: How to save CSS changes of Styles panel](https://stackoverflow.com/questions/6843495/how-to-save-css-changes-of-styles-panel-of-chrome-developer-tools)
  - Workspaces
  - Overrides
- Option 4: Stylus with live editing?
- Option 5: Inject the CSS manually and somehow reload it periodically.

## Icon display

- Option 1: `background` [coloring with data url](https://stackoverflow.com/questions/13367868/modify-svg-fill-color-when-being-served-as-background-image)

```
 	content: "";
  background: transparent url(../assets/toolbar/concept.svg) no-repeat;
  height: 12px;
  width: 12px;
  background-size: contain;
  display: inline-block;
  filter: brightness(1.5);
```

- Option 2: [masks](https://developer.mozilla.org/de/docs/Web/CSS/mask) (supports coloring, care prefixing)

```
  content: "";
  background: green;
  display: inline-block;
  width: 12px;
  height: 12px;
  -webkit-mask-image: url(../assets/toolbar/concept.svg);
  -webkit-mask-repeat: no-repeat;
  -webkit-mask-size: contain;
```

- Option 3: Download, color/resize and host myself or use data url.

## Current RemNote Markup Problems

Right now the styling is not stable. The RemNote's markup is pretty dynamic due to heavy optimization. There are elements created and deleted whenever you hover over a Rem or focus to edit. I might have missed some cases.

There are also some difficulties with the current markup which might get fixed later:

- **Dynamic markup!** I tried to work around a bit, but for example if you hover over rems fast sometimes the hover markup sticks and there are duplicated icons.
- Concepts, descriptors and Questions have an extra tag `span.*_rem_type` with a zero-width-non-breakable space (`&#65279;`) between name and `..`. This might be a bug though. Currently it generates extra icons.
  - Btw: Slots don't.
- Card types are handled differently: For Multiline, Set and List the `:::` is virtual - you can't select it.
- Slots are handled differently than Concept, descriptor and Question. With slots the `::` marker is just text, with the other types, it has its own tag.
- Some things break if you make part of the name of a concept bold.
  - Note to self: This splits the name into multiple tags. This might be the cause why some names in my backup are lists of strings.
  - Those things still get the `.bold` tag which was fixed in [Remnote#58](https://github.com/remnoteio/remnote-issues/issues/58).
  - Styling works when not hovered. When hovered, it is removed.
- Concept etc. get removed when selecting plain, slots don't. I think plain should not remove the card status and just reset List, Set, Multiline.

### WIP: Wishlist for RemNote Team

- [ ] Make `#hierarchy-editor-references` a class, not an id.
- [ ] Remove `&#65279;` tag.
- [ ] Add class to indicate hover, unfocused.
  - There is `.rem-container-focused` for edit
  - E.g. to remove styling when hovered to make `::` editable.
- Design decision: How to handle `::` marker. Is this visual only and changable in menu or with shortcut or should it be editable as text.

  - [ ] Fix Slot handling.
  - [ ] Fix plain.

- [ ] Add a setting to disable Uppercase/lowercase convention for Concept/descriptor and `?` for Question and rely on shortcut/menu to change type.
