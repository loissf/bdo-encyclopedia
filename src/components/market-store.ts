import { ListItem, SubList, SubListItem } from "@/models/Item";
import { getCategory, getItem } from "@/queries";
import { defineStore } from "pinia";
import { ref } from "vue";

export enum ViewType {
  ItemList,
  ItemDetail,
  ItemSubList,
}

export interface Category {
  mainCategory: number;
  subCategory: number;
  items: ListItem[];
}

export const useMarketStore = defineStore("market", () => {
  const selectedCategory = ref<Category>();

  async function selectCategory(selected: {
    mainCategory: number;
    subCategory: number;
  }) {
    const items = await getCategory(
      selected.mainCategory,
      selected.subCategory
    );
    selectedCategory.value = { ...selected, items };
    viewType.value = ViewType.ItemList;
  }

  const selectedItem = ref<SubList>();

  async function selectItem(selected: number) {
    const item = await getItem(selected);
    selectedItem.value = item;
    viewType.value = ViewType.ItemSubList;
  }

  const selectedEnhancement = ref<SubListItem>();

  async function selectEnhancement(selected: SubListItem) {
    selectedEnhancement.value = selected;
    viewType.value = ViewType.ItemDetail;
  }

  const viewType = ref<ViewType>();

  return {
    selectCategory,
    selectedCategory,
    selectItem,
    selectedItem,
    selectedEnhancement,
    selectEnhancement,
    viewType,
  };
});
