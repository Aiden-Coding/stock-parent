import request from '@/config/axios'

export const getIdApi = (): Promise<IResponse> => {
  return request.get({ url: '/stockPicTag/getId' })
}

export const addApi = (data: any): Promise<IResponse> => {
  return request.post({ url: '/stockPicTag/add', data })
}

export const getPicTagApi = (code: string, timespan: string): Promise<IResponse> => {
  return request.get({ url: '/stockPicTag/getPicTag', params: { code, timespan } })
}

export const deleteByIdPicTagApi = (id: string): Promise<IResponse> => {
  return request.delete({ url: `/stockPicTag/deleteById/${id}` })
}
