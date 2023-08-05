import request from '@/config/axios'

export const getMyGroupApi = (): Promise<IResponse> => {
  return request.get({ url: '/userGroup/grouplist' })
}

export const addGroupApi = (data: any): Promise<IResponse> => {
  return request.post({ url: '/userGroup/add', data })
}

export const deleteGroupApi = (data: any): Promise<IResponse> => {
  return request.delete({ url: '/stock/myGroup/delete', data })
}
export const groupStockListApi = (data: any): Promise<IResponse> => {
  return request.post({ url: '/userGroup/groupStock', data })
}

export const addStockApi = (groupId: any): Promise<IResponse> => {
  return request.post({ url: '/stock/myGroup/addStock', groupId })
}

export const deleteStockApi = (groupId: any, code: any): Promise<IResponse> => {
  return request.delete({ url: '/stock/myGroup/deleteStock', groupId, code })
}

export const searchStockApi = (search: any): Promise<IResponse> => {
  return request.get({ url: '/stockBaseInfo/search', params: { search } })
}
