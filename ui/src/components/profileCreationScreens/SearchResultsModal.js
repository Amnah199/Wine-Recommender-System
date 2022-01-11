import {
  CircularProgress,
  ImageListItem,
  Paper,
  Card,
  CardActionArea,
} from "@mui/material";
import { Add } from "@mui/icons-material";
import React, { useContext, useEffect, useState } from "react";
import { SwaggerContext } from "../../App";
import { CustomModal } from "../CustomModal";
import { ImageList, ImageListItemBar } from "@mui/material";
import { CustomImageList } from "../CustomImageList";
import { searchWine } from "../../tempfile";
export const SearchResultModal = (props) => {
  const swagger = useContext(SwaggerContext);
  const [results, setResults] = useState(null);
  useEffect(
    () =>
      swagger.search_wines
        .search_wines_read({ criteria: props.searchString })
        .then((result) => {
          console.log(result.body.wines);
          setResults(result.body.wines);
        }),
    []
  );
  return (
    <CustomModal
      buttonDisabled={true}
      title={"Results for: " + props.searchString}
      onClose={props.onClose}
    >
      {!results ? (
        <CircularProgress />
      ) : (
        <CustomImageList
          button={<Add />}
          data={results}
          id={"id"}
          pictureUrl={"picture_url"}
          label={"name"}
          cols={3}
          onClick={(elem) => props.onClose(elem)}
        />
      )}
    </CustomModal>
  );
};
