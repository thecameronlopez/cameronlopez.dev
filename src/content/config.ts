import { defineCollection, z } from "astro:content";

const projects = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    category: z.enum(["app", "site"]),
    status: z.enum(["live", "wip", "coming-soon"]).default("live"),
    summary: z.string(),
    url: z.string().url().optional(),
    impact: z.array(z.string()).default([]),
    technicalDetails: z.array(z.string()).default([]),
    techStack: z.array(z.string()).default([]),
    screenshots: z
      .array(
        z.object({
          src: z.string(),
          alt: z.string(),
        }),
      )
      .default([]),
    sortOrder: z.number().default(999),
  }),
});

const projectPages = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string().default("Projects"),
    intro: z.string(),
    navGroups: z
      .array(
        z.object({
          id: z.enum(["app", "site"]),
          label: z.string(),
          sortOrder: z.number().default(999),
        }),
      )
      .default([
        { id: "app", label: "Apps", sortOrder: 1 },
        { id: "site", label: "Static Sites", sortOrder: 2 },
      ]),
  }),
});

export const collections = { projects, projectPages };
