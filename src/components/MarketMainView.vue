<template>
  <div class="market">
    <div class="top-bar">
      <TopBar></TopBar>
    </div>
    <div class="categories">
      <CategoriesSelector
        @select:category="selectCategory"
      ></CategoriesSelector>
    </div>
    <div class="content">
      <component :is="viewType"></component>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, watch } from "vue";
import ItemList from "./market-items/ItemList.vue";
import ItemSubList from "./market-items/ItemSubList.vue";
import TopBar from "./TopBar.vue";
import CategoriesSelector from "./categories-selector/CategoriesSelector.vue";
import { getCategory } from "@/queries";

import { useMarketStore, ViewType } from "./market-store";

const marketStore = useMarketStore();

const viewType = computed(() => {
  switch (marketStore.viewType) {
    case ViewType.ItemList:
      return ItemList;
    case ViewType.ItemSubList:
      return ItemSubList;
    default:
      return ItemList;
  }
});

const items = computed({
  get: () => marketStore.listItems,
  set: (value) => (marketStore.listItems = value),
});

async function selectCategory(categoryId: number, subcategoryId: number) {
  items.value = await getCategory(categoryId, subcategoryId);
}
</script>

<style scoped lang="scss">
.market {
  display: grid;
  grid-template:
    "categories top-bar" 1fr
    "categories content" 12fr /
    1fr 3fr;

  overflow: hidden;
  height: 100%;

  .top-bar {
    border: 1px solid white;
    grid-area: top-bar;
  }

  .categories {
    border: 1px solid white;
    grid-area: categories;
    overflow-y: auto;
    overflow-x: hidden;
  }

  .content {
    border: 1px solid white;
    grid-area: content;
    overflow-y: auto;
  }

  *::-webkit-scrollbar {
    width: 6px;
  }

  *::-webkit-scrollbar-track {
    background: #2b2b2b;
  }

  *::-webkit-scrollbar-thumb {
    background-color: #dfb14f;
    border-radius: 10px;
  }
}
</style>
