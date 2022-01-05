import {
  CircularProgress,
  ImageListItem,
  Paper,
  Card,
  CardActionArea,
} from "@mui/material";
import React, { useContext, useEffect, useState } from "react";
import { SwaggerContext } from "../../App";
import { CustomModal } from "../CustomModal";
import { ImageList, ImageListItemBar } from "@mui/material";
import { CustomImageList } from "../CustomImageList";
export const SearchResultModal = (props) => {
  const swagger = useContext(SwaggerContext);
  const [results, setResults] = useState(null);
  useEffect(
    () =>
      swagger
        .search_wines({ search_content: props.searchString })
        .then((result) => console.log(result))
        .catch(() => {
          const result = {
            wines: [
              {
                id: 1,
                name: "2017 Primitivo di Madura",
                picture_url: "http://127.0.0.1:8080/testimage.png",
              },
              {
                id: 5,
                name: "Susumaniello 2020di Epicuro",
                picture_url: "http://127.0.0.1:8080/testimage.png",
              },
              {
                id: 3,
                name: "Susumaniello 2020di Epicuro",
                picture_url: "http://127.0.0.1:8080/testimage.png",
              },
              {
                id: 4,
                name: "Susumaniello 2020di Epicuro",
                picture_url: "http://127.0.0.1:8080/testimage.png",
              },
              {
                id: 2,
                name: "Susumaniello 2020di Epicuro",
                picture_url: "http://127.0.0.1:8080/testimage.png",
              },
            ],
          };
          setResults(result.wines);
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
          data={results}
          id={"id"}
          pictureUrl={"picture_url"}
          label={"name"}
          onClick={(elem) => props.onClose(elem)}
        />
      )}
    </CustomModal>
  );
};
