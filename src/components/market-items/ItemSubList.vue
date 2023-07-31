<template>
  <div v-if="selectedItem" class="item-detail">
    <button type="button" @click="returnClick">Return</button>
    <ListItemComponent
      class="base-item"
      :item="selectedItem.baseItem"
    ></ListItemComponent>
    <ul>
      <li v-for="item in selectedItem.subList" :key="item.id">
        <ListItemComponent :item="item"></ListItemComponent>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import ListItemComponent from "./ListItemComponent.vue";
import { useMarketStore, ViewType } from "@/components/market-store";

const marketStore = useMarketStore();

const selectedItem = marketStore.selectedItem;

function returnClick() {
  marketStore.selectedItem = undefined;
  marketStore.viewType = ViewType.ItemList;
}
</script>

<style scoped lang="scss">
.item-detail {
  .base-item {
    margin-bottom: 1.5rem;
  }
}

ul {
  width: 100%;

  padding: 0;
  margin: 0;

  overflow-y: auto;

  li {
    display: block;
    width: 100%;

    &:not(:last-child) {
      margin-bottom: 0.375rem;
    }
  }
}
</style>
