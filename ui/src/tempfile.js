export const temp_profile = {
  wine_data: [
    {
      selection_type: "multiselect",
      name: "Type of Wine",
      options: [
        { option: "red", selected: false },
        { option: "white", selected: true },
        { option: "sparkling", selected: false },
      ],
    },
    {
      selection_type: "multiselect",
      name: "Price",
      options: [
        { option: "under 10€", selected: false },
        { option: "10-20€", selected: true },
        { option: "over 20€", selected: true },
      ],
    },
    {
      selection_type: "search_field",
      name: "Origin",
      options: [
        { option: "Germany", selected: true },
        { option: "Italy", selected: true },
        { option: "France", selected: false },
      ],
    },
  ],
  taste_data: [
    { label: "tree fruit", percentage: 0.2 },
    { label: "red fruit", percentage: 0.1 },
    { label: "citrus fruit", percentage: 0.5 },
    { label: "cinnamon", percentage: 0.3 },
  ],
};

export const searchWine = {
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

export const recos = {
  sellers: [
    {
      rank: 1,
      id: 1,
      name: "Jacques",
      lat: "51.94",
      lon: "7.65",
      info: [
        { label: "address", content: "Spiegelturm 2 48143 Münster" },
        { label: "whatever", content: "info we have on the wineseller" },
      ],
    },
    {
      rank: 2,
      id: 3,
      name: "second seller",
      lat: "51.95",
      lon: "7.66",
      info: [
        { label: "address", content: "Spiegelturm 2 48143 Münster" },
        { label: "whatever", content: "info we have on the wineseller" },
      ],
    },
    {
      rank: 3,
      id: 2,
      name: "third seller",
      lat: "51.96",
      lon: "7.64",
      info: [
        { label: "address", content: "Spiegelturm 2 48143 Münster" },
        { label: "whatever", content: "info we have on the wineseller" },
      ],
    },
  ],
  wines: [
    {
      rank: 1,
      id: 1,
      name: "abcd",
      picture_url: "http://127.0.0.1:8080/testimage.png",
    },
    {
      rank: 2,
      id: 4,
      name: "asdasd",
      picture_url: "http://127.0.0.1:8080/testimage.png",
    },
    {
      rank: 3,
      id: 3,
      name: "xcv",
      picture_url: "http://127.0.0.1:8080/testimage.png",
    },
    {
      rank: 4,
      id: 2,
      name: "xcvxvc",
      picture_url: "http://127.0.0.1:8080/testimage.png",
    },
    {
      rank: 5,
      id: 5,
      name: "xcvxvc",
      picture_url: "http://127.0.0.1:8080/testimage.png",
    },
    {
      rank: 6,
      id: 6,
      name: "xcvxvc",
      picture_url: "http://127.0.0.1:8080/testimage.png",
    },
  ],
};

export const wineData = {
  id: 1,
  name: "Primitivo di Madura 2013",
  picture_url: "http://127.0.0.1:8080/testimage.png",
  description:
    "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
  facts: [
    { label: "region", content: "italy, puglia" },
    { label: "style", content: "red" },
    { label: "alc", content: "12%" },
  ],
  taste_data: [
    { label: "tree fruit", percentage: 0.2 },
    { label: "red fruit", percentage: 0.1 },
    { label: "citrus fruit", percentage: 0.5 },
    { label: "cinnamon", percentage: 0.3 },
  ],
};
