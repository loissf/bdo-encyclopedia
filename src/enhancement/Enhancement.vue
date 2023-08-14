<template>
  <div>
    <input type="text" name="search-box" id="search-box" v-model="searchTerm" />
    <ul v-if="searchResult">
      <li v-for="item in searchResult" :key="item.id">
        <img class="icon" :src="item.icon" alt="" />
        <span class="name">{{ item.name }}</span>
      </li>
    </ul>
  </div>
  <EnhancementView :enhancement="enhancement" />
</template>

<script setup lang="ts">
import { ref, watch } from "vue";

import items from "@/resources/items.json";
import { DictionaryItem } from "@/models/Item";

import EnhancementView from "./EnhancementView.vue";
import { Enhancement } from "./Process";

const enhancement = ref<Enhancement>(
  new Enhancement(
    [
      {
        id: 11630,
        name: "Laytenn's Power Stone",
        grade: 3,
        enhancement: 0,
        quantity: 1,
      },
    ],
    [
      {
        id: 11630,
        name: "Laytenn's Power Stone",
        grade: 3,
        enhancement: 4,
        quantity: 1,
      },
    ],
    {
      id: 11630,
      name: "Laytenn's Power Stone",
      grade: 3,
      enhancement: 3,
      quantity: 1,
    },
    55
  )
);

const searchTerm = ref<string>("");

const searchResult = ref<DictionaryItem[]>();

watch(searchTerm, (value) => {
  if (!value) {
    searchResult.value = [];
    return;
  }

  searchResult.value = search(value);
});

function search(term: string) {
  return Object.values(items)
    .filter((x) =>
      decodeHtmlCharCodes(x.name).toLowerCase().includes(term.toLowerCase())
    )
    .slice(0, 100)
    .map(
      (x) =>
        ({
          id: parseInt(x.id),
          name: x.name,
          grade: parseInt(x.grade),
          icon: `https:\\cdn.arsha.io/icons/${x.id}.png`,
          mainCategory: x.main_category,
          subCategory: x.sub_category,
        } as DictionaryItem)
    );
}

function decodeHtmlCharCodes(str: string) {
  return str.replace(/(&#(\d+);)/g, function (match, capture, charCode) {
    return String.fromCharCode(charCode);
  });
}
</script>

<style scoped lang="scss"></style>
