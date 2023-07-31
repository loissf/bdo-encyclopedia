<template>
  <div class="item-search">
    <input
      type="text"
      name="search-input"
      id="search-input"
      v-model="searchTerm"
    />
    <button type="button" @click="search">search</button>
  </div>
</template>

<script setup lang="ts">
import { ListItem } from "@/models/Item";
import { getItemSearch } from "@/queries";
import { ref } from "vue";
import items from "../resources/items.json";
import { useMarketStore } from "./market-store";

const marketStore = useMarketStore();

const searchTerm = ref<string>("");

async function search() {
  const ids = Object.values(items)
    .filter((x) =>
      decodeHtmlCharCodes(x.name)
        .toLowerCase()
        .includes(searchTerm.value.toLowerCase())
    )
    .map((x) => parseInt(x.id));
  marketStore.listItems = await getItemSearch(ids);
}

function decodeHtmlCharCodes(str: string) {
  return str.replace(/(&#(\d+);)/g, function (match, capture, charCode) {
    return String.fromCharCode(charCode);
  });
}
</script>
