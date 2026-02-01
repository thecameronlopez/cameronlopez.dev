import React from "react";
import { Outlet } from "react-router-dom";

const RootLayout = () => {
  return (
    <>
      <header>
        <h1>Cameron Lopez</h1>
      </header>
      <main>
        <Outlet />
      </main>
      <footer>
        <p>cameronlopez.dev</p>
      </footer>
    </>
  );
};

export default RootLayout;
