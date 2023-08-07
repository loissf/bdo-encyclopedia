<template>
  <div class="item-search">
    <select name="grade" id="grade-select" v-model="selectedGrade">
      <option value="">All</option>
      <option value="0">White</option>
      <option value="1">Green</option>
      <option value="2">Blue</option>
      <option value="3">Yellow</option>
      <option value="4">Red</option>
    </select>
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
import { ref } from "vue";
import items from "../resources/items.json";
import { useMarketStore } from "./market-store";

const marketStore = useMarketStore();

const searchTerm = ref<string>("");

const selectedGrade = ref<string>("");

async function search() {
  if (!searchTerm.value) {
    return;
  }
  const ids = Object.values(items)
    .filter(
      (x) =>
        decodeHtmlCharCodes(x.name)
          .toLowerCase()
          .includes(searchTerm.value.toLowerCase()) &&
        (selectedGrade.value != "" ? x.grade === selectedGrade.value : true)
    )
    .map((x) => parseInt(x.id));

  await marketStore.searchItems(ids);
}

function decodeHtmlCharCodes(str: string) {
  return str.replace(/(&#(\d+);)/g, function (match, capture, charCode) {
    return String.fromCharCode(charCode);
  });
}
</script>
