import React, { useEffect, useState } from 'react';
import { Route } from 'react-router';
import {
  Navigate,
  useNavigate
} from "react-router-dom";

const RouteGaurd = ({ children, pageConfig }) => {
  return (
    <React.Fragment>
      {children}
    </React.Fragment>
  )
}

export const getRoute = (pageConfig) => {
  const { path, element, layout: Layout } = pageConfig;
  let _element;
  _element = Layout ? <Layout>{element}</Layout> : element;
  _element = <RouteGaurd pageConfig={pageConfig}>{_element}</RouteGaurd>;

  return <Route path={path} element={_element} key={path} />;
}