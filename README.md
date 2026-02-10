# cameronlopez.dev

Portfolio site built with Astro.

## Commands

```sh
npm install
npm run dev
npm run build
npm run preview
```

## Projects System (Content Collections)

Project pages are content-driven and generated dynamically from:

- `src/content/config.ts`
- `src/content/projects/*.md`
- `src/pages/projects/[slug].astro`
- `src/layout/ProjectLayout.astro`
- `src/content/projectPages/projects.md` (projects page intro + nav groups)

## Add a New Project Checklist

1. Create a new content file in `src/content/projects/` (example: `my-project.md`).
2. Add required frontmatter fields:
   - `title`
   - `category` (`app` or `site`)
   - `summary`
3. Add optional fields as needed:
   - `status` (`live`, `wip`, `coming-soon`)
   - `url`
   - `impact` (array)
   - `technicalDetails` (array)
   - `techStack` (array)
   - `screenshots` (array of `{ src, alt }`)
   - `sortOrder` (number)
4. If using screenshots, place files under `public/screenshots/...` and reference with absolute paths like `/screenshots/my-project/shot-1.png`.
5. Run `npm run build` to validate schema and route generation.
6. Visit `/projects` and `/projects/<slug>` to verify nav ordering and page content.

## Edit Projects Page Intro / Nav Labels

Update `src/content/projectPages/projects.md`:

- `intro` controls the summary paragraph on `/projects`.
- `navGroups` controls project group labels and their order in sidebar/select.
