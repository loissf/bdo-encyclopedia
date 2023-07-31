<template>
  <div class="market">
    <div class="top-bar">
      <TopBar />
    </div>
    <div class="categories">
      <CategoriesSelector />
    </div>
    <div class="content">
      <component v-if="viewType" :is="viewType" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import ItemList from "./market-items/ItemList.vue";
import ItemSubList from "./market-items/ItemSubList.vue";
import TopBar from "./TopBar.vue";
import CategoriesSelector from "./categories-selector/CategoriesSelector.vue";

import { useMarketStore, ViewType } from "./market-store";
import ItemDetail from "./market-items/ItemDetail.vue";

const marketStore = useMarketStore();

const viewType = computed(() => {
  switch (marketStore.viewType) {
    case ViewType.ItemList:
      return ItemList;
    case ViewType.ItemSubList:
      return ItemSubList;
    case ViewType.ItemDetail:
      return ItemDetail;
  }
});
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
