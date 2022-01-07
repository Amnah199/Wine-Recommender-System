import React, { useState, Fragment } from "react";
import { Typography } from "@mui/material";
import { CustomModal } from "../CustomModal";
import { MultiSelect } from "../selectors/MultiSelect.js";
import { SearchMultiSelect } from "../selectors/SearchMultiSelect.js";
import { PinDropSharp } from "@mui/icons-material";

export const ProfileCustomization = (props) => {
  return (
    <>
      {props.profile.wine_data.map((elem, index) => {
        let onChange = (change) => {
          let index = props.profile.wine_data.indexOf(elem);
          let newProfile = props.profile;
          let newElem = elem;
          newElem.options = change;
          newProfile.wine_data[index] = newElem;
          props.onProfileChange(newProfile);
        };

        if (elem.selection_type == "multiselect") {
          return (
            <Fragment key={index}>
              <MultiSelect
                label={elem.name}
                options={elem.options}
                onChange={onChange}
              />
            </Fragment>
          );
        } else if (elem.selection_type == "search_field") {
          return (
            <Fragment key={index}>
              <SearchMultiSelect
                options={elem.options}
                getOptionLabel={(elem) => elem.option}
                label={elem.name}
                onChange={onChange}
              />
            </Fragment>
          );
        }
      })}
    </>
  );
};
