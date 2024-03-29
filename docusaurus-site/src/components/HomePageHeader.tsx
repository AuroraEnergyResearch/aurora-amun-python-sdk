import React from "react";
import clsx from "clsx";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import styles from "./styles.module.css";

const HomePageHeader = () => {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={clsx("hero hero--primary", styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg margin-right--md"
            to="/docs/intro"
          >
            Getting Started
          </Link>
          <Link
            className="button button--secondary button--lg margin-right--md"
            to="/docs/Examples/Load Factors/common"
          >
            Examples
          </Link>
          <Link
            className="button button--secondary button--lg margin-right--md"
            to="/docs/Reference/parameters"
          >
            SDK Reference
          </Link>
          <Link
            className="button button--secondary button--lg margin-right--md"
            to="/docs/changelog"
          >
            Changelogs
          </Link>
        </div>
      </div>
    </header>
  );
}

export default HomePageHeader;