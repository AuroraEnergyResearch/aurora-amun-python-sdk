// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const themes = require("prism-react-renderer")
const fs = require("fs");
const path = require("path");


const getSDKVersion = () => {
  const setupFilePath = path.resolve(__dirname, '../setup.py');
  const setupFileContent = fs.readFileSync(setupFilePath, 'utf8');
  const versionMatch = setupFileContent.match(/version="(.*)"/);

  if (!versionMatch) {
    throw new Error('Could not extract SDK version from setup.py');
  }

  return versionMatch[1];
}

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Aurora Amun SDK Docs",
  tagline: "Python software development kit documentation for Amun",
  favicon: "img/favicon.ico",

  // Set the production url of your site here
  url: "https://auroraenergyresearch.github.io",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/aurora-amun-python-sdk/",

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "AuroraEnergyResearch", // Usually your GitHub org/user name.
  projectName: "aurora-amun-python-sdk", // Usually your repo name.

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: "img/logo.png",
      tableOfContents: {
        minHeadingLevel: 2,
        maxHeadingLevel: 5,
      },
      navbar: {
        title: "Aurora Amun SDK Docs",
        logo: {
          alt: "Aurora Energy Research Logo",
          src: "img/logo.svg",
        },
        items: [
          {
            type: "docSidebar",
            sidebarId: "docSidebar",
            position: "left",
            label: "Docs",
          },
          {
            href: "/",
            label: `SDK Version: ${getSDKVersion()}`,
            position: "left",
          },
          {
            href: "https://github.com/AuroraEnergyResearch/aurora-amun-python-sdk",
            label: "GitHub",
            position: "right",
          },
        ],
      },
      footer: {
        style: "dark",
        copyright: `Copyright © ${new Date().getFullYear()} Aurora Energy Research. Built with Docusaurus.`,
      },
      prism: {
        theme: themes.themes.github,
        darkTheme: themes.themes.dracula
      },
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false,
        respectPrefersColorScheme: false,
      },
    }),
};

module.exports = config;
