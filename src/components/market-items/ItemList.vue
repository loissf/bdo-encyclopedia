<template>
  <div class="item-list">
    <ul>
      <li v-for="item in items" :key="item.id">
        <ListItemComponent
          :item="item"
          @click="selectItem(item)"
        ></ListItemComponent>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { ListItem } from "@/models/Item";
import ListItemComponent from "./ListItemComponent.vue";
import { getItem } from "@/queries";
import { useMarketStore, ViewType } from "@/components/market-store";

const marketStore = useMarketStore();

const items = computed({
  get: () => marketStore.listItems,
  set: (value) => (marketStore.listItems = value),
});

async function selectItem(item: ListItem) {
  const selectedItem = (await getItem(item.id)) ?? {
    baseItem: item,
    subList: [],
  };

  marketStore.selectedItem = selectedItem;

  marketStore.viewType =
    selectedItem.subList.length > 1
      ? ViewType.ItemSubList
      : ViewType.ItemDetail;
}
</script>

<style scoped lang="scss">
.item-list {
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
